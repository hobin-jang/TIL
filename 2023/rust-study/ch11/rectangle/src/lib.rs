#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle {
            width: 5,
            height: 10,
        };
        let smaller = Rectangle {
            width: 3,
            height: 1,
        };

        assert!(larger.can_hold(&smaller));
        assert!(!smaller.can_hold(&larger));
    }
}
