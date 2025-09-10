use futures::executor::block_on;
use pyo3::prelude::*;
use sea_query::{Expr, ExprTrait, Query, SqliteQueryBuilder};
use sqlx::{Pool, Sqlite};

use crate::core::Tasks;

// <·
type Task = (i32, String, String);

#[pyclass]
pub struct TasksDB {
    pub pool: Pool<Sqlite>,
}

#[pymethods]
impl TasksDB {
    #[new]
    pub fn new() -> Self {
        let pool = futures::executor::block_on(async { TasksDB::get_pool().await });

        let _ = TasksDB::create_table(&pool);

        Self { pool: pool }
    }

    fn create(&self, title: String, content: String) -> PyResult<Task> {
        let sql = Query::insert()
            .into_table(Tasks::Table)
            .columns([Tasks::Title, Tasks::Content])
            .values_panic([title.into(), content.into()])
            .returning_all()
            .to_string(SqliteQueryBuilder);

        let res = block_on(async {
            sqlx::query_as::<_, Task>(&sql)
                .fetch_one(&self.pool)
                .await
                .unwrap()
        });

        Ok(res)
    }

    fn read_all(&self) -> PyResult<Vec<Task>> {
        let sql = Query::select()
            .columns([Tasks::Id, Tasks::Title, Tasks::Content])
            .from(Tasks::Table)
            .to_string(SqliteQueryBuilder);

        let res = block_on(async {
            sqlx::query_as::<_, Task>(&sql)
                .fetch_all(&self.pool)
                .await
                .unwrap()
        });

        Ok(res)
    }

    fn read_one(&self, id: i32) -> PyResult<Task> {
        let sql = Query::select()
            .columns([Tasks::Id, Tasks::Title, Tasks::Content])
            .and_where(Expr::col(Tasks::Id).eq(Expr::val(id)))
            .from(Tasks::Table)
            .to_string(SqliteQueryBuilder);

        let res = block_on(async {
            sqlx::query_as::<_, Task>(&sql)
                .fetch_one(&self.pool)
                .await
                .unwrap()
        });

        Ok(res)
    }

    fn update(&self, t: Task) -> PyResult<Option<Task>> {
        let sql = Query::update()
            .table(Tasks::Table)
            .values([(Tasks::Title, t.1.into()), (Tasks::Content, t.2.into())])
            .and_where(Expr::col(Tasks::Id).eq(Expr::val(t.0)))
            .returning_all()
            .to_string(SqliteQueryBuilder);

        let res = block_on(async {
            sqlx::query_as::<_, Task>(&sql)
                .fetch_optional(&self.pool)
                .await
                .unwrap()
        });

        Ok(res)
    }

    fn delete(&self, id: i32) -> PyResult<u64> {
        let sql = Query::delete()
            .from_table(Tasks::Table)
            .and_where(Expr::col(Tasks::Id).eq(Expr::val(id)))
            .to_string(SqliteQueryBuilder);

        let res = block_on(async {
            sqlx::query(&sql)
                .execute(&self.pool)
                .await
                .unwrap()
                .rows_affected()
        });

        Ok(res)
    }
}
