use std::{fs::read_to_string};

fn main() -> std::io::Result<()> {
    let input = read_to_string("../input").unwrap();
    let mut number_elves: Vec<i32> = Vec::new();
    let mut sum = 0;

    for i in input.lines() {
        if i.is_empty() {
            number_elves.push(sum);
            sum = 0;        
        } else {
            sum += i.parse::<i32>().unwrap();
        }
    }
    number_elves.sort();
    number_elves.reverse();
    sum = number_elves.iter().take(3).sum();
    println!("{}", sum);
    Ok(())
}
