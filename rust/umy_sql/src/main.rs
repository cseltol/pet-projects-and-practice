use mysql::*;
use mysql::prelude::*;

#[derive(Debug, PartialEq, Eq)]
struct Dev {
    country_id: i32,
    salary: i32,
    lang: Option<String>,
}



fn main() -> Result<()> {
    let url = "mysql://root:PASSWORD@127.0.0.1:3306/dbx";
    let opts = Opts::from_url(url)?;
    let pool = Pool::new(opts)?;

    let mut conn = pool.get_conn()?;

    conn.query_drop(
        r"CREATE TEMPORARY TABLE dev (
            country_id int not null,
            salary int not null,
            lang text
        )"
    )?;

    let devs = vec![
        Dev {country_id: 1, salary: 10_000, lang: None},
        Dev {country_id: 2, salary: 100_000, lang: Some("Rust".into())},
        Dev {country_id: 3, salary: 90_000, lang: Some("Go".into())},
    ];

    conn.exec_batch(r"INSERT INTO dev (country_id, salary, lang)
        VALUES (:country_id, :salary, :lang)",
devs.iter().map(|p| params! {
        "country_id" => p.country_id,
        "salary" => p.salary,
        "lang" => &p.lang,
    })).unwrap();

    let selected_devs = conn
        .query_map("SELECT country_id, salary, lang FROM dev"
        , |(country_id, salary, lang)| {
            Dev {country_id, salary, lang}
    })?;

    assert_eq!(devs, selected_devs);
    println!("Successefully write and read to temporary table!");

    Ok(())
}