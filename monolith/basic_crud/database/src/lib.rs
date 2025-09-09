use pyo3::prelude::*;

mod app;
mod core;

#[pymodule]
fn main(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(app::create, m)?)?;
    m.add_function(wrap_pyfunction!(app::read, m)?)?;
    m.add_function(wrap_pyfunction!(app::delete, m)?)?;
    m.add_function(wrap_pyfunction!(app::update, m)?)?;
    Ok(())
}
