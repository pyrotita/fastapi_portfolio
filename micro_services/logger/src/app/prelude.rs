use actix_web::{web, Responder, HttpResponse};

// .?
use crate::types::log::Log;

// <·
pub async fn create_log(data: web::Json<Log>) -> impl Responder {
    todo!("Unimplemented!")
}
