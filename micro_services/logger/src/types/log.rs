use actix_web::{error, Error};
use serde::Deserialize;

//<·
#[derive(Debug, Deserialize)]
pub struct Log {
    pub entity: String,
    pub date: String,
}

impl Log {
    pub fn validate(self) -> Result<(), Error> {
        Ok(())
    }
}
