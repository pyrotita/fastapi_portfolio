use sea_query::{Iden, SqliteQueryBuilder, Table};
use sqlx::sqlite::SqlitePoolOptions;
use sqlx::{Pool, Sqlite}

//<·
#[derive(Debug, Iden)]
pub enum Logs {
    Table,
    Id,
    Author,
    Content,
    Date,
}
