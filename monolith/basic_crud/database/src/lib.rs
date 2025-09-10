use pyo3::prelude::*;

mod core;
mod py_lib;

#[pymodule]
fn database(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<crate::py_lib::TasksDB>()?;

    Ok(())
}
