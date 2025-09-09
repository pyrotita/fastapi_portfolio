use pyo3::prelude::*;
use sea_query::{Expr, ExprTrait};
use sea_query::{Query, SqliteQueryBuilder};
use sqlx::sqlite::SqlitePoolOptions;
use sqlx::{Pool, Sqlite};

//~>
use crate::core::Tasks;

type PyModel = (i32, String, String);

#[pyclass]
pub struct TasksDB {
    pool: Pool<Sqlite>,
}

#[pymethods]
impl TasksDB {
    #[new]
    fn new() -> Self {
        let pool = SqlitePoolOptions::new()
            .max_connections(5)
            .connect(db_url)
            .await
            .unwrap();

        Self { pool: pool }
    }
}

#[pyfunction]
pub async fn create(pool: &Pool<Sqlite>, title: String, content: String) -> PyModel {
    let sql = Query::insert()
        .into_table(Tasks::Table)
        .columns([Tasks::Id, Tasks::Title, Tasks::Content])
        .values_panic([title.into(), content.into()])
        .returning_all()
        .to_string(SqliteQueryBuilder);

    sqlx::query_as::<_, PyModel>(&sql)
        .fetch_one(pool)
        .await
        .unwrap()
}

#[pyfunction]
pub async fn read(pool: &Pool<Sqlite>) -> Vec<PyModel> {
    let sql = Query::select()
        .columns([Tasks::Id, Tasks::Title, Tasks::Content])
        .from(Tasks::Table)
        .to_string(SqliteQueryBuilder);

    sqlx::query_as::<_, PyModel>(&sql)
        .fetch_all(pool)
        .await
        .unwrap()
}

#[pyfunction]
pub async fn update(
    pool: &Pool<Sqlite>,
    iden: i32,
    title: String,
    content: String,
) -> Option<PyModel> {
    let sql = Query::update()
        .table(Tasks::Table)
        .values([
            (Tasks::Title, title.into()),
            (Tasks::Content, content.into()),
        ])
        .and_where(Expr::col(Tasks::Id).eq(Expr::val(iden)))
        .returning_all()
        .to_string(SqliteQueryBuilder);

    sqlx::query_as::<_, PyModel>(&sql)
        .fetch_optional(pool)
        .await
        .unwrap()
}

#[pyfunction]
pub async fn delete(pool: &Pool<Sqlite>, id: i32) -> u64 {
    let sql = Query::delete()
        .from_table(Tasks::Table)
        .and_where(Expr::col(Tasks::Id).eq(Expr::val(id)))
        .to_string(SqliteQueryBuilder);

    sqlx::query(&sql)
        .execute(pool)
        .await
        .unwrap()
        .rows_affected()
}
