use env_logger::{Builder, Target};
use log::{Level, Metadata, Record, SetLoggerError};

fn log_message(_msg: &str) {
    // by default log level is `ERROR`
    // any lower levels are dropped
    log::debug!("Message: {}", _msg);  
}

fn do_smth(_msg: &str) -> Result<(), &'static str> {
    Err("Can't do it")
}

struct ConsoleLogger;
static CONSOLE_LOGGER: ConsoleLogger = ConsoleLogger;

impl log::Log for ConsoleLogger {
    fn enabled(&self, metadata: &Metadata) -> bool {
        metadata.level() <= Level::Info
    }
    fn log(&self, record: &Record) {
        if self.enabled(record.metadata()) {
            println!("Rust says: {} - {}", record.level(), record.args());
        }
    }
    fn flush(&self) {}
}

fn main() -> Result<(), SetLoggerError> {
    env_logger::init();
    // log debug info to the console
    log_message("Debug");

    // log an error message to the console
    let res = do_smth("error message");
    if let Err(err) = res {
        log::error!("Failed: {}", err)
    }

    // log to stdout instead of stderr
    Builder::new()
    .target(Target::Stdout)
    .init();

    log::error!("This error has been printed to Stdout");

    // log message with custom logger
    log::set_logger(&CONSOLE_LOGGER)?;
    log::set_max_level(log::LevelFilter::Info);

    log::info!("log info");
    log::warn!("warn");
    log::error!("error");

    Ok(())
}
