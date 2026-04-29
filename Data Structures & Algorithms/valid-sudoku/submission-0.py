class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    def get_box_index(row, col):
      return (row // 3) * 3 + (col // 3)

    complete_box = [set() for _ in range(9)]
    complete_row = [set() for _ in range(9)]
    complete_column = [set() for _ in range(9)]

    for row_number, row_data in enumerate(board):
      for col_number, col_data in enumerate(row_data):
        if col_data == '.': continue
        if (
          col_data in complete_column[col_number]
          or col_data in complete_row[row_number]
          or col_data in complete_box[get_box_index(row_number, col_number)]
        ):
          print(f"Row : {row_number} Col: {col_number} Box: {get_box_index(row_number, col_number)}")
          return False

        complete_column[col_number].add(col_data)
        complete_row[row_number].add(col_data)
        complete_box[get_box_index(row_number, col_number)].add(col_data)

    return True
