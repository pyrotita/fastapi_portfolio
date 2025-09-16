use actix_web::{web, App, HttpServer};

// ~>
mod app;
mod data;
mod sec;
mod type;

// .?
use crate::app::prelude;

// <·
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/", web::post().to(prelude::create_log))
            .route("/", web::get().to(prelude::read_log))
            .route("/all", web::get().to(prelude::read_logs))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
