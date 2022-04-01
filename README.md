# Auto sudoku.com

This tool can automatically play sudoku on sudoku.com with an extremely speed.
How it works?
- It captures the board from sudoku.com and saves it
<img width="584" alt="original" src="https://user-images.githubusercontent.com/75875212/128294885-2a414030-d65c-4961-a416-bd1efe4957ef.png">

- Then it converts the image into a 9x9 array by detecting where are blanks, where are numbers (and what those number are).
<img width="540" alt="detect" src="https://user-images.githubusercontent.com/75875212/128294626-f9b0ec56-5f57-40e9-8d38-8e1050d6538c.png">

- Solve the board and autofill on sudoku.com

To use this tool, you have to locate x, y, width, height and center of the first cell of the board on your screen,.
(use run locate.py and follow its instruction to locate those positions) 
  
  
Result:

<img width="744" alt="z" src="https://user-images.githubusercontent.com/75875212/128297383-7011ef74-7767-4a3a-a2fc-02dd712e530e.png">
