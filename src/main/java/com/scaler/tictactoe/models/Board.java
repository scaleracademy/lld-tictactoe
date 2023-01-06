package com.scaler.tictactoe.models;

import java.util.List;

public class Board {
    private List<List<Cell>> board;

    public List<List<Cell>> getBoard() {
        return board;
    }

    public void setBoard(List<List<Cell>> board) {
        this.board = board;
    }
}
