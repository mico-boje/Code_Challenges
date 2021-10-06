// mod semi_structured_logs;
// use semi_structured_logs::LogLevel;

// mod factory;
mod digital_root;



fn main() {
//     // let a = semi_structured_logs::log(LogLevel::Error, "test");
//     // println!("{}", a)
//     let a = factory::working_items_per_minute(5);
//     println!("{}", a);
//     println!("{}", factory::production_rate_per_hour(6));
//     println!("{:?}", f64::EPSILON);
    println!("{}", digital_root::digital_root(157));
 }
