
#include <iostream>
#include <string>
#include <assert.h>
#include <ctype.h>

using namespace std;

const int NUM_ROWS = 8;
const int NUM_COLS = 8;


// **************** CLASS: CELL *******************
class Cell {
	char piece;
	char color;
public:
	Cell();
	void place(char color, char piece);
	string take();
	string getPiece();
	string look();
};

Cell::Cell() {
	piece = ' ';
	color = ' ';
}

string Cell::look() {
	string result = "";
	result = result.append(1, color);
	result = result.append(1, piece);
	return result;
}

string Cell::take() {
	string result = look();
	piece = ' ';
	color = ' ';
	return result;
}

void Cell::place(char newColor, char newPiece) {
	assert((newColor == 'W') || (newColor == 'B'));
	color = newColor;
	assert((newPiece == 'R') || (newPiece == 'K') || (newPiece == 'B') || (newPiece == 'Q') || (newPiece == 'K') || (newPiece == 'N') || (newPiece == 'P'));
	piece = newPiece;

}

string Cell::getPiece() {
	string result = "";
	result = result.append(1, color);
	result = result.append(1, piece);
	return result;
}

// **************** CLASS: BOARD *******************
class Board {
	Cell board[NUM_ROWS][NUM_COLS]; // <-- Not a good idea in the long run
	void displayLine();
	bool moveRook(int row, int col, string direction, int steps);
	bool movePawn(int row, int col, string direction, int steps);
	bool moveBishop(int row, int col, string direction, int steps);
	bool moveQueen(int row, int col, string direction, int steps);
	bool moveKing(int row, int col, string direction, int steps);
	bool moveKnight(int row, int col, string direction, int steps);
public:
	Board(string = "WITHPAWNS");
	Board(string, int, int, char, char); // Constructor for board with only one piece
	void displayBoard();
	void place(int, int, char, char);
	string take(int, int);
	bool cellEmpty(int, int);
	string look(int, int);
	bool pawnTP(int, int, string);
	bool movePieceOneStep(string, string, int&, int&);
	bool movePiece(int row, int col, string direction, int steps);
	bool turn(int row, int col, string direction, int numSpaces);
	
};

bool Board::cellEmpty(int row, int col) {
	if (board[row][col].getPiece() == "  ")
		return true;
	return false;
}

void Board::place(int row, int col, char color, char peice) {
	assert((row >= 0) && (row < NUM_ROWS));
	assert((col >= 0) && (col < NUM_COLS));
	board[row][col].place(color, peice);

}

string Board::look(int row, int col) {
	assert((row >= 0) && (row < NUM_ROWS));
	assert((col >= 0) && (col < NUM_COLS));
	return board[row][col].look();

}
string Board::take(int row, int col) {
	assert((row >= 0) && (row < NUM_ROWS));
	assert((col >= 0) && (col < NUM_COLS));
	return board[row][col].take();

}
Board::Board(string command, int row, int col, char color, char piece) {
	if (command == "ONEPIECE") {
		board[row][col].place(color, piece);
		return;
	}
}
Board::Board(string command) {
	board[0][0].place('B', 'R');
	board[0][1].place('B', 'N');
	board[0][2].place('B', 'B');
	board[0][3].place('B', 'Q');
	board[0][4].place('B', 'K');
	board[0][5].place('B', 'B');
	board[0][6].place('B', 'N');
	board[0][7].place('B', 'R');
	if (command != "NOPAWNS") {
		for (int c = 0; c < NUM_COLS; c++) {
			board[1][c].place('B', 'P');
		}
	}

	board[NUM_ROWS - 1][0].place('W', 'R');
	board[NUM_ROWS - 1][1].place('W', 'N');
	board[NUM_ROWS - 1][2].place('W', 'B');
	board[NUM_ROWS - 1][4].place('W', 'K');
	board[NUM_ROWS - 1][3].place('W', 'Q');
	board[NUM_ROWS - 1][5].place('W', 'B');
	board[NUM_ROWS - 1][6].place('W', 'N');
	board[NUM_ROWS - 1][7].place('W', 'R');
	if (command != "NOPAWNS") {
		for (int c = 0; c < NUM_COLS; c++) {
			board[NUM_COLS - 2][c].place('W', 'P');
		}
	}

}
void Board::displayLine() {
	cout << endl;
	for (int x = 0; x < NUM_COLS+1; x++) {
		cout << "    | ";
	}
	cout << endl;
	for (int x = 0; x < NUM_COLS+1; x++) {
		cout << "----| ";
	}
	cout << endl;

}

void Board::displayBoard() {
	//return; // DEBUG
	cout << endl << "CURRENT BOARD:" << endl << endl;
	char row = 'A'-1;
	for (int r = 0; r < NUM_ROWS+1; r++) {
		for (int c = 0; c < NUM_COLS+1; c++) {
		    if(r==0 && c==0)
		        cout<< " "<< "  "<<" | ";
		    else if(r==0)
		        cout<<" "<< c-1<< " "<<" | ";
		    else if(c==0)
		        cout<<" "<< (char)(row+r)<< " "<< " | ";
		    else 
			    cout << " " << board[r-1][c-1].getPiece() << " | ";
			    
		}
	
		displayLine();
	}
	
	cout << endl << endl;
}

bool Board::movePieceOneStep(string piece, string direction, int &row, int &col) {
	assert((row >= 0) && (row < NUM_ROWS));
	assert((col >= 0) && (col < NUM_COLS));
	int toRow = row;
	int toCol = col;
	if (direction == "S")
		toRow = row + 1;
	else if (direction == "N")
		toRow = row - 1;
	else if (direction == "E")
		toCol = col + 1;
	else if (direction == "W")
		toCol = col - 1;
	else if (direction == "NW") {
		toRow = row - 1;
		toCol = col - 1;
	}
	else if (direction == "NE") {
		toRow = row - 1;
		toCol = col + 1;
	}
	else if (direction == "SW") {
		toRow = row + 1;
		toCol = col - 1;
	}
	else if (direction == "SE") {
		toRow = row + 1;
		toCol = col + 1;
	}
	else {
		cout << "INVALID DIRECTION!" << endl;
		assert(false); // force a failure
	}

	assert((toRow >= 0) && (toRow < NUM_ROWS));
	assert((toCol >= 0) && (toCol < NUM_COLS));

    string toPiece = look(toRow, toCol);
    
    if (!cellEmpty(toRow, toCol) && toPiece.at(0)==piece.at(0)) {
		cout << "Space [ " << toRow << ", " << toCol <<
			"] Contains [" << look(toRow, toCol) << "]" << endl;
			take(row,col);
		return false;
	}
	else if (!cellEmpty(toRow, toCol) && toPiece.at(0)!=piece.at(0) && piece.at(1)!='P') {
		take(row, col);
		place(toRow,toCol,piece.at(0), piece.at(1));
		return true;
	}
	else if(!cellEmpty(toRow, toCol) && piece.at(1)=='P')
	{
	    cout<<"You can't take a piece like that with a Pawn"<<endl;
	    return false;
	}
	
	piece = take(row, col);
	place(toRow, toCol, piece.at(0), piece.at(1));
	row = toRow;
	col = toCol;

	return true;
}

bool Board::moveQueen(int row, int col, string direction, int steps) {
	string piece = look(row, col);
	assert(piece.at(1) == 'Q');

	for (int x = 0; x < steps; x++) {
		if (!movePieceOneStep(piece, direction, row, col))
			return false;
	}
	return true;
}

bool Board::moveKing(int row, int col, string direction, int steps) {
	string piece = look(row, col);
	assert(piece.at(1) == 'K');

	if (steps > 1) {
		cout << "Kings can not move " << steps << " steps at a time!" << endl;
		return false;
	}

	if (!movePieceOneStep(piece, direction, row, col))
			return false;

	return true;
}

bool Board::moveBishop(int row, int col, string direction, int steps) {
	string piece = look(row, col);
	assert(piece.at(1) == 'B');

	if (!((direction == "NE") || (direction == "SE") || (direction == "NW") || (direction == "SW"))) {
		cout << "Bishops can not move " << direction << "!" << endl;
		return false;
	}
	for (int x = 0; x < steps; x++) {
		if (!movePieceOneStep(piece, direction, row, col))
			return false;
	}
	return true;
}

bool Board::moveRook(int row, int col, string direction, int steps) {
	string piece = look(row, col);
	assert(piece.at(1) == 'R');

	if (!((direction == "N") || (direction == "S") || (direction == "W") || (direction == "E"))) {
		cout << "Rooks can not move " << direction << "!" << endl;
		return false;
	}
	for (int x = 0; x < steps; x++) {
		if (!movePieceOneStep(piece, direction, row, col))
			return false;
	}
	return true;
}
bool Board::moveKnight(int row, int col, string direction, int steps) {
	string piece = look(row, col);
	assert(piece.at(1) == 'N');

	if (steps > 1) {
		cout << "Knights can not move " << steps << " steps at a time!" << endl;
		return false;
	}
	int toRow = row;
	int toCol = col;
	if (direction == "NNE") {
		toRow -= 2;
		toCol += 1;
	}
	else if (direction == "NEE") {
		toRow -= 1;
		toCol += 2;
	}
	else if (direction == "SEE") {
		toRow += 1 ;
		toCol += 2;
	}
	else if (direction == "SSE") {
		toRow += 2 ;
		toCol += 1;
	}
	else if (direction == "SSW") {
		toRow += 2;
		toCol -= 1;
	}
	else if (direction == "SWW") {
		toRow += 1;
		toCol -= 2;
	}
	else if (direction == "NWW") {
		toRow -= 1;
		toCol -= 2;
	}
	else if (direction == "NNW") {
		toRow -= 2;
		toCol -= 1;
	}
	else {
		cout << "Knights can not move " << direction << "!" << endl;
		return false;
	}
    
    string toPiece = look(toRow, toCol);
    
    if (!cellEmpty(toRow, toCol) && toPiece.at(0)==piece.at(0)) {
		cout << "Space [ " << toRow << ", " << toCol <<
			"] Contains [" << look(toRow, toCol) << "]" << endl;
			
		return false;
	}

	piece = take(row, col);
	place(toRow, toCol, piece.at(0), piece.at(1));

	return true;
}
bool Board::pawnTP(int row, int col, string dir){
    int toRow=0, toCol=0;
    string piece;
    
    if (dir == "NW") {
		toRow = row - 1;
		toCol = col - 1;
	}
	else if (dir == "NE") {
		toRow = row - 1;
		toCol = col + 1;
	}
	else if (dir == "SW") {
		toRow = row + 1;
		toCol = col - 1;
	}
	else if (dir == "SE") {
		toRow = row + 1;
		toCol = col + 1;
	}
    
    if(cellEmpty(toRow, toCol)){
        cout<<"There was no piece to take"<<endl;
        return false;
    }
    else{
    cout<<"Attempting to take "<< look(toRow, toCol)<< " at ["<<toRow<<","<<toCol<<"]"<<endl;
    piece = take(row, col);
	place(toRow, toCol, piece.at(0), piece.at(1));
    }
    return true;
    
}
bool Board::movePawn(int row, int col, string direction, int steps) {
	string piece = look(row, col);
	assert(piece.at(1) == 'P');
    
    if((piece.at(0) == 'W') && ((direction == "NW") || (direction == "NE"))){
        return pawnTP(row, col,direction);
    }
	if ((piece.at(0) == 'W') && (direction != "N")) {
		cout << "White pawns can not move " << direction << "!" << endl;
		return false;
	}
	if((piece.at(0) == 'B') && ((direction == "SW") || (direction == "SE"))){
	    return pawnTP(row, col,direction);
	}
	if ((piece.at(0) == 'B') && (direction != "S")) {
		cout << "Black pawns can not move " << direction << "!" << endl;
		return false;
	}
	if (steps > 2) {
		cout << "Pawns can not move " << steps << " steps at a time!" << endl<<endl;
		return false;
	}
	if(row>1 && row<5 && steps>1)
	{
	    cout<< "Pawns can only move 1 step after their first move!"<<endl;
	    return false;
	}
	for (int x = 0; x < steps; x++) {
		if (!movePieceOneStep(piece, direction, row, col))
			return false;
	}
	return true;
}

bool Board::movePiece(int row, int col, string direction, int steps) {
	string piece = look(row, col);
	
	if (piece.at(1) == 'R')
		return moveRook(row, col, direction, steps);
	else if (piece.at(1) == 'P')
		return movePawn(row, col, direction, steps);
	else if (piece.at(1) == 'B')
		return moveBishop(row, col, direction, steps);
	else if (piece.at(1) == 'Q')
		return moveQueen(row, col, direction, steps);
	else if (piece.at(1) == 'K')
		return moveKing(row, col, direction, steps);
	else if (piece.at(1) == 'N')
		return moveKnight(row, col, direction, steps);
	else {
		cout << "Invalid piece " << piece << " at position [" << row << ", " << col << "]" << endl;
		assert(false);
	}
	return true;
}

bool Board::turn(int row, int col, string direction, int numSpaces) {
	if ((row < 0) || (row >= NUM_ROWS)) {
		cout << "OUT OF BOUNDS!" << endl;
		assert(false); // temporary
		return false;
	}
	if ((col < 0) || (col >= NUM_COLS)) {
		cout << "OUT OF BOUNDS!" << endl;
		assert(false); // temporary
		return false;
	}
	
	string piece = look(row,col);
	
	
	if (!movePiece(row, col, direction, numSpaces)) {
		place(row, col, piece.at(0), piece.at(1));
		return false;
	}
	
	
	displayBoard();

	return true;
}

bool mated()
{
    return false;
}

string getPosition()
{
    string pos;
    cout<<"Enter cell (row/col) to move:"<<endl;
    cin>>pos;
    return pos;
    
}

string getDir()
{
    string dir;
    cout<<"Enter direction:"<<endl;
    cin>>dir;
    return dir;
    
}
int getSteps()
{
    int steps;
    cout<<"Enter number of steps:"<<endl;
    cin>>steps;
    return steps;
    
}
bool getTurn(bool turn)
{
    if(turn){
        cout<<"White's Turn!"<<endl;
        return true;
     }
    else
    { cout<<"Black's Turn!"<<endl;
        return false;
    }
}

bool makeMove(Board& board, char color)
{
    int row, col, steps;
    string dir, pos;
    bool turn;
    bool sCNT=true;
    
    
    do{
        if(color=='W'){
            turn = true;
            turn = getTurn(turn);}
        else{
            turn =false;
        turn = getTurn(turn);}
        
        pos = getPosition();
        
        
        row = pos.at(0)-65;
        col = pos.at(1)-48;
        dir = getDir();
        steps = getSteps();
        
        if(row>7 || col>7)
        {
            cout<<"***Error: Please enter a valid row/col"<<endl;
            return false;
        }
            
       string pc = board.look(row,col);
       
       
        if(color == pc.at(0))
            sCNT=true;
        else 
            sCNT=false;
            
            
        if(sCNT ==false)
            cout<<"Oops, attempt to move out of turn please select the right color piece"<<endl;
                
     
    }while(sCNT==false || !board.turn(row, col, dir, steps));
    
    

    
    
    
    return true;
    
}

int main() {

	Board board;
	string goOn = "";
	cout << "BEGINNING BOARD:" << endl;
	board.displayBoard();
	while ((goOn != "N") && (goOn != "n")) {
		while (!makeMove(board, 'W'))
			;
		while (!makeMove(board, 'B'))
			;
		cout << "Continue? (Y/N) ";
		cin >> goOn;
	}

	cout << "ENDING BOARD:" << endl;
	board.displayBoard();
	return 0;
}
