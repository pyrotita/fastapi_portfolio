use sea_query::{ColumnDef, Iden, SqliteQueryBuilder, Table};
use sqlx::{Pool, Sqlite};

// create table function
pub async fn create_table(pool: &Pool<Sqlite>) {
    let sql = Table::create()
        .table(Tasks::Table)
        .if_not_exists()
        .col(
            ColumnDef::new(Tasks::Id)
                .unique_key()
                .integer()
                .not_null()
                .auto_increment(),
        )
        .col(ColumnDef::new(Tasks::Title).string().not_null())
        .col(ColumnDef::new(Tasks::Content).string().not_null())
        .to_string(SqliteQueryBuilder);

    sqlx::query(&sql).execute(pool).await.unwrap();
}

// model table
#[derive(Debug, Iden)]
pub enum Tasks {
    Table,
    Id,
    Title,
    Content,
}
