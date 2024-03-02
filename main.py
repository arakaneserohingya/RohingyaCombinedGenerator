# List of strings
strings = [
    "𐴉𐴥𐴠𐴓𐴝𐴘 𐴊𐴞𐴘𐴧𐴠",
    "𐴈𐴡𐴔",
    "𐴁𐴝𐴙𐴄𐴧𐴝𐴒𐴡𐴌𐴥𐴡𐴕",
    "𐴁𐴝𐴙𐴄𐴧𐴝",
    "𐴀𐴠𐴌𐴞 𐴊𐴦𐴡𐴕",
    "𐴉𐴠𐴍",
    "𐴉𐴠𐴍𐴡𐴌",
    "𐴊𐴦𐴝𐴉𐴥𐴝𐴘𐴓𐴡𐴘𐴎𐴦𐴡𐴕 𐴒𐴥𐴡𐴘",
    "𐴄𐴤𐴡𐴌𐴦𐴡𐴕",
    "𐴃𐴝𐴑𐴡𐴃𐴢",
    "𐴈𐴝𐴔𐴡𐴃𐴢 𐴀𐴝𐴕𐴦𐴡𐴕",
    "𐴒𐴟𐴏𐴡𐴓𐴢",
    "𐴏𐴥𐴝𐴉𐴢 𐴒𐴡𐴌𐴥𐴠𐴉𐴥𐴠𐴓",
    "𐴉𐴥𐴠𐴓𐴝𐴘 𐴊𐴥𐴠",
    "𐴁𐴝𐴁𐴟𐴃𐴠",
    "𐴖𐴡𐴌𐴠",
    "𐴒𐴡𐴐𐴝𐴈𐴝𐴀𐴘 𐴀𐴤𐴡𐴊𐴠 𐴕𐴞𐴐𐴝𐴥𐴕",
    "𐴈𐴡𐴃𐴡𐴔𐴞𐴑𐴧𐴝",
    "𐴒𐴝𐴙𐴌 𐴇𐴝𐴎𐴠𐴌",
    "𐴒𐴝𐴙𐴓𐴊𐴡𐴦𐴕",
    "𐴒𐴡𐴏𐴥𐴞𐴓𐴡",
    "𐴓𐴟𐴖𐴝𐴎𐴝",
    "𐴑𐴡𐴁𐴟𐴓 𐴒𐴡𐴌𐴥𐴡𐴕",
    "𐴑𐴡𐴁𐴟𐴓 𐴒𐴡𐴙𐴅𐴧𐴝",
    "𐴌𐴝𐴏𐴧𐴝",
    "𐴀𐴠𐴏𐴃𐴝𐴔𐴥𐴝𐴓 𐴒𐴡𐴌𐴞𐴁𐴝𐴌 𐴐𐴥𐴞𐴐",
    "𐴔𐴡𐴏𐴞𐴁𐴡𐴃𐴢",
    "𐴀𐴝𐴃𐴥𐴞𐴑𐴧𐴝",
    "𐴄𐴥𐴡𐴌𐴥𐴡𐴕"
]

# Write strings to a .combine file
# with open("rohingya.combine", "w", encoding="utf-8") as file:
#     for string in strings:
#         file.write(string + "\n")
#

# Write data to a dictionary file
with open("rohingya.combined", "w", encoding="utf-8") as file:
    file.write("dictionary=main:rhg,locale=rhg,description=Rohingya wordlist. Author: Ahkter Husin <arkaneserohingya1@gmail.com>,date=02132024,version=1\n")
    for string in strings:
        file.write(string + "\n")

    # for string in strings:
    #     file.write(f'{string}\n')

    # for index, string in enumerate(strings):
    #     file.write(f'word_{index} = "{string}"\n')