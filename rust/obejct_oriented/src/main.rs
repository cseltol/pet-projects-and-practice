mod private_dev {
    use chrono::Utc;

    pub struct Project {
        pub members: Vec<Box<dyn TeamMember>>,
    }
    pub trait TeamMember {
        fn do_task(&self) {
            println!("Do task {}", Utc::now())
        }
    }

    pub struct Dev {
        lang: String,
        exp: i32,
        tasks: Vec<String>,
    }

    pub struct Qa {

    }

    impl TeamMember for Qa {}

    impl TeamMember for Dev {
        fn do_task(&self) {
            println!("Do dev task {}", Utc::now())
        }
    }

    impl Dev {
        pub fn new(lang: String) -> Dev {
            Dev {
                lang: lang,
                exp: 0,
                tasks: Vec::new(),
            }
        }

        pub fn change_lang(&mut self, new_lang: String) {
            if new_lang == "C++".to_string() {
                self.lang = new_lang;
            }
        }

        fn list_tasks(&self) -> &Vec<String> {
            &self.tasks
        }
    }
}

fn main() {
    let mut dev = private_dev::Dev::new("Rust".to_string());
    dev.change_lang( "C#".to_string());
    
    let qa = private_dev::Qa{};

    let mut project = private_dev::Project {
        members: Vec::new(), 
    };

    project.members.push(Box::new(dev));
    project.members.push(Box::new(qa));

    for i in project.members.iter() {
        i.do_task();
    }
}
