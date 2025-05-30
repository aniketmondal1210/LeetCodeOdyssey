# Problem: Defanging an IP Address

## Problem Statement
Given a valid IPv4 address `address`, return a defanged version of that IP address.  
A defanged IP address replaces every period `"."` with `"[.]"`.  

## Constraints
- The given `address` is a valid IPv4 address.

## Examples

### Example 1
- **Input:** `address = "1.1.1.1"`
- **Output:** `"1[.]1[.]1[.]1"`

### Example 2
- **Input:** `address = "255.100.50.0"`
- **Output:** `"255[.]100[.]50[.]0"`
