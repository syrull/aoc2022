use std::{fs::read_to_string};

fn part_one(input: String) -> i32 {
    let mut player_score = 0;
    for line in input.lines() {
        let our_choice = &line[2..3];
        let enemy_choice = &line[..1];
        match &our_choice {
            &"X" => {
                if enemy_choice == "C" {
                    player_score += 7
                } else if enemy_choice == "A" {
                    player_score += 4
                } else {
                    player_score += 1
                }
            },
            &"Y" => {
                if enemy_choice == "A" {
                    player_score += 8
                } else if enemy_choice == "B" {
                    player_score += 5
                } else {
                    player_score += 2
                }
            },
            &_ => {
                if enemy_choice == "B" {
                    player_score += 9
                } else if enemy_choice == "C" {
                    player_score += 6
                } else {
                    player_score += 3
                }
            }
        }
    }
    player_score
}

fn part_two(input: String) -> i32 {
    let mut player_score = 0;
    for line in input.lines() {
        let our_choice = &line[2..3];
        let enemy_choice = &line[..1];
        match &our_choice {
            &"X" => {
                if enemy_choice == "C" {
                    player_score += 2
                } else if enemy_choice == "A" {
                    player_score += 3
                } else {
                    player_score += 1
                }
            },
            &"Y" => {
                if enemy_choice == "A" {
                    player_score += 4
                } else if enemy_choice == "B" {
                    player_score += 5
                } else {
                    player_score += 6
                }
            },
            &_ => {
                if enemy_choice == "B" {
                    player_score += 9
                } else if enemy_choice == "C" {
                    player_score += 7
                } else {
                    player_score += 8
                }
            }
        }
    }
    player_score
}

fn main() {
    let input = read_to_string("../input").unwrap();
    println!("Part 1: {}", part_one(input.clone()));
    println!("Part 2: {}", part_two(input));
}
