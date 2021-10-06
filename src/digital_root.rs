
pub fn digital_root(n: i64) -> i64 {
    let str_n = n.to_string();
    compute_result(str_n)
}

fn compute_result(mut str_n: String) -> i64 {
    let mut result: i64 = 0;
    while str_n.len() > 1 {
        let mut numbers = vec![];
        let split = str_n.split("");
        for s in split {
            let f = s.parse::<i64>();
            let f = match f {
                Ok(f) => f,
                Err(_) => 0
            };
            numbers.push(f);
        };
        result = numbers.iter().sum();
        str_n = result.to_string();
    }
    result
}

