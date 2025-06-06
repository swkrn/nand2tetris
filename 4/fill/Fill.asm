// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.

// NOTE: This code just fills the screen. It does not listen to the keyboard.
@16384
D=A
@0
M=D

(LOOP)
D=0
D=!D

@0
A=M
M=D

@0
M=M+1

D=M
@24576
D=A-D

@LOOP
D;JGT

(END)
@END
0;JMP