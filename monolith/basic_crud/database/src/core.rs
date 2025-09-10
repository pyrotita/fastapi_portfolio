use sea_query::{Iden, SqliteQueryBuilder, Table};
use sqlx::{sqlite::SqlitePoolOptions, Pool, Sqlite};

// local
use crate::py_lib::TasksDB;

// <·
#[derive(Debug, Iden)]
pub enum Tasks {
    Table,
    Id,
    Title,
    Content,
}

impl TasksDB {
    fn get_database_url() -> String {
        dotenvy::dotenv().ok();

        std::env::var("DATABASE_URL").unwrap_or("sqlite://do.db".into())
    }

    pub async fn get_pool() -> Pool<Sqlite> {
        let database_url = TasksDB::get_database_url();

        SqlitePoolOptions::new()
            .max_connections(5)
            .connect(&database_url)
            .await
            .unwrap()
    }

    pub async fn create_table(pool: &Pool<Sqlite>) -> Result<(), String> {
        use sea_query::ColumnDef;

        let sql = Table::create()
            .table(Tasks::Table)
            .if_not_exists()
            .col(
                ColumnDef::new(Tasks::Id)
                    .integer()
                    .primary_key()
                    .auto_increment(),
            )
            .col(ColumnDef::new(Tasks::Title).text().not_null())
            .col(ColumnDef::new(Tasks::Content).text().not_null())
            .to_string(SqliteQueryBuilder);

        sqlx::query(&sql).execute(pool).await.unwrap();
        Ok(())
    }
}
