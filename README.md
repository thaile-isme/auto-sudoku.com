# destroy_sudoku

This tool can automatically play sudoku on sudoku.com with an extremely speed.
How it works?
- First, it captures the board from sudoku.com and save it
<img width="584" alt="original" src="https://user-images.githubusercontent.com/75875212/128294885-2a414030-d65c-4961-a416-bd1efe4957ef.png">

- Then it convert image to an 9x9 array by detecting where is blank, where is number (and what that number is).
<img width="540" alt="detect" src="https://user-images.githubusercontent.com/75875212/128294626-f9b0ec56-5f57-40e9-8d38-8e1050d6538c.png">

- Solve the board and autofill on sudoku.com

To use this tool, you have to:
  + locate x, y, width, height of the board on our screen.
  + locate center of the first cell as well.
(use run locate.py and follow its instruction to locate those positions) 
  
  
Result:

<img width="744" alt="z" src="https://user-images.githubusercontent.com/75875212/128297383-7011ef74-7767-4a3a-a2fc-02dd712e530e.png">
