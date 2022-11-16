if __name__ == "__main__":
    with open("E:\\code\\other\\self\\operating-system\\c\\clean\\start.asm", "w") as fw:
        with open("E:\\code\\other\\self\\operating-system\\c\\nasm\\start.asm", "r") as fr:
            content = fr.readline()
            while content:
                if content.startswith("global") or content.startswith("extern"):
                    content = fr.readline()
                    continue
                content = content.replace("noexecute", "")
                content = content.replace("execute", "")
                fw.write(content)
                content = fr.readline()
