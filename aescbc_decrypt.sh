#!/bin/bash

for i in {0..23}
do
    for j in {0..59}
    do
        key="2024-02-14 $(printf "%02d" $i):$(printf "%02d" $j)"
        iv="superdupersecretIV"
        echo "Trying: $key, $iv"
        key_hex=$(printf "%s" "$key" | xxd -p)
        iv_hex=$(printf "%s" "$iv" | xxd -p)
        echo "Key hex $key_hex, IV hex $iv_hex"
        openssl aes-128-cbc -d -in encrypted_file.dat -out "decrypted_files/$i$j" -K "$key_hex" -iv "$iv_hex"
        file_output=$(file decrypted_files/$i$j)
        if [[ $file_output == *"data"* ]]; then
            #rm decrypted_files/$i$j
            continue
        else
            echo "Possible key: $key"
        fi
    done
done
