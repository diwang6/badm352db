with open("data_injection.txt", 'r') as command_file:
    with open("script.txt", 'w') as script_file:
        for line in command_file:
            line = line.strip()
            script_file.write('cur.execute("'+line+'")\n')