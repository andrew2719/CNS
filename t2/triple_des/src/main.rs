use des::Des;
use des::cipher::{BlockEncrypt, BlockDecrypt, KeyInit};
use des::cipher::generic_array::GenericArray;
use std::io::{self, Write};

struct TripleDes {
    des1: Des,
    des2: Des,
    des3: Des,
}

impl TripleDes {
    fn new(key: &[u8; 24]) -> Self {
        TripleDes {
            des1: Des::new_from_slice(&key[0..8]).unwrap(),
            des2: Des::new_from_slice(&key[8..16]).unwrap(),
            des3: Des::new_from_slice(&key[16..24]).unwrap(),
        }
    }

    fn encrypt_block(&self, block: &mut [u8; 8]) {
        let mut block = GenericArray::from_mut_slice(block);
        self.des1.encrypt_block(&mut block);
        self.des2.decrypt_block(&mut block);
        self.des3.encrypt_block(&mut block);
    }

    fn decrypt_block(&self, block: &mut [u8; 8]) {
        let mut block = GenericArray::from_mut_slice(block);
        self.des3.decrypt_block(&mut block);
        self.des2.encrypt_block(&mut block);
        self.des1.decrypt_block(&mut block);
    }

    fn encrypt(&self, data: &[u8]) -> Vec<u8> {
        let mut padded = data.to_vec();
        let padding_len = 8 - (padded.len() % 8);
        padded.extend(std::iter::repeat(padding_len as u8).take(padding_len));
        
        for chunk in padded.chunks_mut(8) {
            self.encrypt_block(chunk.try_into().unwrap());
        }
        padded
    }

    fn decrypt(&self, data: &[u8]) -> Vec<u8> {
        let mut decrypted = data.to_vec();
        for chunk in decrypted.chunks_mut(8) {
            self.decrypt_block(chunk.try_into().unwrap());
        }
        let padding_len = *decrypted.last().unwrap() as usize;
        decrypted.truncate(decrypted.len() - padding_len);
        decrypted
    }
}

fn bytes_to_hex(bytes: &[u8]) -> String {
    bytes.iter().map(|b| format!("{:02x}", b)).collect()
}

fn main() {
    let key = [
        1, 2, 3, 4, 5, 6, 7, 8,
        9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19, 20, 21, 22, 23, 24
    ];
    let triple_des = TripleDes::new(&key);

    println!("Enter the text to encrypt:");
    io::stdout().flush().unwrap();

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let input = input.trim();

    let data = input.as_bytes();
    println!("Original text: {}", input);
    println!("Original bytes (hex): {}", bytes_to_hex(data));

    let encrypted = triple_des.encrypt(data);
    println!("Encrypted data (hex): {}", bytes_to_hex(&encrypted));

    let decrypted = triple_des.decrypt(&encrypted);
    println!("Decrypted bytes (hex): {}", bytes_to_hex(&decrypted));
    println!("Decrypted text: {}", String::from_utf8_lossy(&decrypted));
}