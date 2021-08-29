""" solution to Day 20a of Advent of Code 2020: https://adventofcode.com/2020/day/20 """

class tiles:
    def __init__(self,id,rows):
        self.id = int(id)
        self.rows = rows
        self.edge1 = rows[0][0] + rows[1][0] + rows[2][0] + rows[3][0] + rows[4][0] + rows[5][0] + rows[6][0] + rows[7][0] + rows[8][0] + rows[9][0]
        self.edge2 = rows[0][0] + rows[0][1] + rows[0][2] + rows[0][3] + rows[0][4] + rows[0][5] + rows[0][6] + rows[0][7] + rows[0][8] + rows[0][9]
        self.edge3 = rows[0][9] + rows[1][9] + rows[2][9] + rows[3][9] + rows[4][9] + rows[5][9] + rows[6][9] + rows[7][9] + rows[8][9] + rows[9][9]
        self.edge4 = rows[9][0] + rows[9][1] + rows[9][2] + rows[9][3] + rows[9][4] + rows[9][5] + rows[9][6] + rows[9][7] + rows[9][8] + rows[9][9]
        self.edge5 = self.edge1[::-1]
        self.edge6 = self.edge2[::-1]
        self.edge7 = self.edge3[::-1]
        self.edge8 = self.edge4[::-1]

    def is_match(self,match):
        if match == self.edge1:
            return True
        elif match == self.edge2:
            return True
        elif match == self.edge3:
            return True
        elif match == self.edge4:
            return True
        elif match == self.edge5:
            return True
        elif match == self.edge6:
            return True
        elif match == self.edge7:
            return True
        elif match == self.edge8:
            return True
        else:
            return False

def match_edges(arr):
    i = 0
    corner_ids = []
    while i < len(arr):
        j = 0 

        matching_edges = []
        while j < len(arr):
           if j == i:
               j += 1
           else:
               if arr[j].is_match(arr[i].edge1):
                   if "1" not in matching_edges:
                       matching_edges.append("1")
               if arr[j].is_match(arr[i].edge2):
                   if "2" not in matching_edges:
                       matching_edges.append("2")
               if arr[j].is_match(arr[i].edge3):
                   if "3" not in matching_edges:
                       matching_edges.append("3")
               if arr[j].is_match(arr[i].edge4):
                   if "4" not in matching_edges:
                       matching_edges.append("4")
               if arr[j].is_match(arr[i].edge5):
                   if "5" not in matching_edges:
                       matching_edges.append("5")
               if arr[j].is_match(arr[i].edge6):
                   if "6" not in matching_edges:
                       matching_edges.append("6")
               if arr[j].is_match(arr[i].edge7):
                   if "7" not in matching_edges:
                       matching_edges.append("7")
               if arr[j].is_match(arr[i].edge8):
                   if "8" not in matching_edges:
                       matching_edges.append("8")
               j += 1
        if len(matching_edges) == 4:
            corner_ids.append(arr[i].id)
        i += 1
    return corner_ids[0] * corner_ids[1] * corner_ids[2] * corner_ids[3]

with open("day-20.txt") as file:
    d = file.readlines()

new_arr = []

for line in d:
    new_arr.append(line.strip())

i = 0

tile_list = []

while i < len(new_arr):
    title_new = new_arr[i]
    title_bits = title_new.split(" ")
    title_id = title_bits[1][0:-1]
    new_rows = [new_arr[i+1].strip(),new_arr[i+2].strip(),new_arr[i+3].strip(),new_arr[i+4].strip(),new_arr[i+5].strip(),new_arr[i+6].strip(),new_arr[i+7].strip(),new_arr[i+8].strip(),new_arr[i+9].strip(),new_arr[i+10].strip()]
    tile_list.append(tiles(title_id,new_rows))
    i += 12

print(match_edges(tile_list))
