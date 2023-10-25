#include <graphics.h>
#include <conio.h>

int main() {

  // Khởi tạo chế độ đồ họa
  int gdriver = DETECT, gmode;
  initgraph(&gdriver, &gmode, "");

  // Vẽ câu a)
  setcolor(YELLOW);
  line(50, 150, 50, 50); // x(n)
  line(100, 100, 100, 50); // x(n-1)  
  line(150, 75, 150, 50); // x(n-3)

  line(50, 125, 50, 25); // y(n)
  line(100, 75, 100, 25);
  line(150, 50, 150, 25);

  outtextxy(20, 160, "Cau a)");

  // Vẽ câu b)
  setcolor(CYAN);

  line(250, 150, 250, 50); // x(n) 
  line(300, 100, 300, 50); // x(n-1)
  line(350, 75, 350, 50); // x(n-2)

  line(250, 100, 250, 25); // y(n-2)
  line(300, 125, 300, 75); // y(n-1)
  line(350, 150, 350, 100); // y(n)

  outtextxy(220, 160, "Cau b)");

  getch();
  closegraph();
  
  return 0;
}