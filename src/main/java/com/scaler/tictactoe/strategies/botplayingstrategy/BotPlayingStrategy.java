package com.scaler.tictactoe.strategies.botplayingstrategy;

import com.scaler.tictactoe.models.Board;
import com.scaler.tictactoe.models.Move;
import com.scaler.tictactoe.models.Player;

public interface BotPlayingStrategy {

    Move decideMove(Player player,Board board);
}
