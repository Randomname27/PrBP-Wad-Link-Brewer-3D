#!/usr/bin/env python3
import argparse
import sys

def generate_xml(wadname, wadfile, wadauthor, waddesc, iwadpath, game_choice):
    if game_choice == 1:
        doomiwadname = "DOOM 1"
        doomver = "doom.wad"
    elif game_choice == 2:
        doomiwadname = "DOOM 2"
        doomver = "doom2.wad"
    else:
        raise ValueError("Invalid game choice, must be 1 (DOOM 1) or 2 (DOOM 2)")

    fullxml = f"""<shortcut>
    <executable>/3ds/PrBoom-Plus.3dsx</executable>
    <arg>-iwad {iwadpath}{doomver} -file {wadfile}</arg>
    <name>{doomiwadname} {wadname} (PrBoom+)</name>
    <description>{waddesc}</description>
    <author>Voxel9, PrBoom+ contributors, {wadauthor} (WAD)</author>
</shortcut>"""
    
    wadfilef = wadfile.replace(".wad", "")
    xmlfn = f"(PrBoom+) {doomiwadname}_{wadfilef}.xml"

    with open(xmlfn, "w") as f:
        f.write(fullxml)

    return xmlfn

def prompt_if_missing(value, prompt_text):
    if value is None:
        return input(prompt_text + ": ").strip()
    return value

def main():
    parser = argparse.ArgumentParser(description="PrB+ Wad Link Brewer 3D - CLI XML generator")
    parser.add_argument("--name", help="Wad Name")
    parser.add_argument("--file", help="Wad File (.wad)")
    parser.add_argument("--author", help="Wad Author")
    parser.add_argument("--description", help="Wad Description")
    parser.add_argument("--iwad", help="IWad Path (directory path)")
    parser.add_argument("--game", type=int, choices=[1, 2], help="Game choice: 1 = DOOM 1, 2 = DOOM 2")

    args = parser.parse_args()

    # Prompt interactively for missing arguments
    wadname = prompt_if_missing(args.name, "Enter Wad Name")
    wadfile = prompt_if_missing(args.file, "Enter Wad File (.wad)")
    wadauthor = prompt_if_missing(args.author, "Enter Wad Author")
    waddesc = prompt_if_missing(args.description, "Enter Wad Description")
    iwadpath = prompt_if_missing(args.iwad, "Enter IWad Path (directory path)")

    if args.game is None:
        while True:
            try:
                game_choice = int(input("Choose Game (1 = DOOM 1, 2 = DOOM 2): ").strip())
                if game_choice in [1, 2]:
                    break
            except ValueError:
                pass
            print("Invalid choice, please enter 1 or 2.")
    else:
        game_choice = args.game

    try:
        xmlfn = generate_xml(wadname, wadfile, wadauthor, waddesc, iwadpath, game_choice)
        print(f"[+] XML file created: {xmlfn}")
    except Exception as e:
        print(f"[!] Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

