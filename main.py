import pygame as pg

from pprint import pprint
import os

class Mouse:
    def __init__(self) -> None:
        self.rel = pg.Vector2(0, 0)
        self.pressed = [False, False, False]
        self.screen_position = pg.Vector2(0, 0)
        self.relative_position = pg.Vector2(0, 0)
        self.grid_position = pg.Vector2(0, 0)
    
    def update(self, offset: pg.Vector2, render_size: int) -> None:
        self.rel = pg.Vector2(pg.mouse.get_rel())
        self.pressed = pg.mouse.get_pressed()
        self.screen_position = pg.mouse.get_pos()
        self.relative_position = self.screen_position - offset
        self.grid_position = self.relative_position // render_size

class App:
    def __init__(self) -> None:
        # constants
        self.RES = self.WIDTH, self.HEIGHT = (1000, 800)
        self.FPS = 60
        
        self.COLORS = {
            0: [0, 0, 0], # empty
            1: [255, 255, 255], # tile
            2: [39, 139, 245], # obstacle
            3: [28, 252, 3], # spawn
            4: [196, 6, 6] # goal
        }
        
        # attributes
        self.render_size = 50
        self.width = 5
        self.height = 5
        self.map = [[0] * self.width for _ in range(self.height)]
        
        self.offset = pg.Vector2(self.WIDTH // 2 - self.width*self.render_size//2, self.HEIGHT // 2 - self.height*self.render_size//2)
        self.selected = 0
        
        # subclasses
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.mouse = Mouse()
    
    def add_row(self) -> None:
        self.height += 1
        self.map.append([0] * self.width)
    
    def add_col(self) -> None:
        self.width += 1
        for y in range(len(self.map)):
            self.map[y].append(0)
    
    def remove_row(self) -> None:
        self.height -= 1
        self.map.pop()
    
    def remove_col(self) -> None:
        self.width -= 1
        for y in range(len(self.map)):
            self.map[y].pop()
    
    def export(self) -> None:
        # flatten the map
        flattened = []
        for row in reversed(self.map):
            flattened.extend(row)
        
        # check valid amount of spawns and goals
        if flattened.count(3) > 2 or flattened.count(3) == 0:
            print("INVALID NUMBER OF SPAWNS")
            return
        if flattened.count(4) != 1:
            print("INVALID NUMBER OF GOALS")
            return
        
        # extract obstacle data
        obstacles = []
        for index, tile in enumerate(flattened):
            if tile == 2:
                flattened[index] = 1
                obstacles.append(index + 1)
        
        # extract spawn data
        spawns = []
        for index, tile in enumerate(flattened):
            if tile == 3:
                flattened[index] = 1
                spawns.append(index + 1)
        if len(spawns) == 1:
            spawns *= 2
        
        # extract goal data
        goals = []
        for index, tile in enumerate(flattened):
            if tile == 4:
                flattened[index] = 1
                goals.append(index + 1)
        
        # insert map size data
        flattened.insert(0, self.height)
        flattened.insert(0, self.width)
        
        # write data
        with open("out/map.txt", "w") as f:
            f.write(" ".join(list(map(str, flattened))))
        
        with open("out/goal-list.txt", "w") as f:
            f.write(" ".join(list(map(str, spawns + goals))))
        
        with open("out/obstacles.txt", "w") as f:
            f.write(" ".join(list(map(str, obstacles))))
        
        os.system("clear")
        pprint(self.map)
        print(f"Obstacles: {obstacles}")
        print(f"Spawns: {spawns + goals}")
        print("EXPORT SUCCESSFUL")
    
    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            
            # keybinds
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.selected = 0
                if event.key == pg.K_2:
                    self.selected = 1
                if event.key == pg.K_3:
                    self.selected = 2
                if event.key == pg.K_4:
                    self.selected = 3
                if event.key == pg.K_5:
                    self.selected = 4
                if event.key == pg.K_z:
                    self.remove_row()
                if event.key == pg.K_c:
                    self.add_row()
                if event.key == pg.K_q:
                    self.remove_col()
                if event.key == pg.K_e:
                    self.add_col()
                if event.key == pg.K_RETURN:
                    self.export()
    
    def update(self) -> None:
        # update mouse
        self.mouse.update(self.offset, self.render_size)

        # tile placing
        if self.mouse.pressed[0]:
            if self.mouse.grid_position[1] >= 0 and self.mouse.grid_position[1] <= self.height - 1:
                if self.mouse.grid_position[0] >= 0 and self.mouse.grid_position[0] <= self.width - 1:
                    self.map[int(self.mouse.grid_position[1])][int(self.mouse.grid_position[0])] = self.selected
        
        # camera movement
        if self.mouse.pressed[1]:
            self.offset += self.mouse.rel
    
    def render(self) -> None:
        # clear screen
        self.screen.fill((0, 0, 0))
        
        # render map3
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                # draw tile outline
                pg.draw.rect(self.screen, (255, 255, 255), [
                    x*self.render_size + self.offset.x,
                    y*self.render_size + self.offset.y,
                    self.render_size,
                    self.render_size
                ], 1)
                
                # draw tile
                if tile != 0:
                    pg.draw.rect(self.screen, self.COLORS[tile], [
                        x*self.render_size + self.offset.x,
                        y*self.render_size + self.offset.y,
                        self.render_size,
                        self.render_size
                    ])
            
        # draw mouse hover tile
        if self.mouse.grid_position[1] >= 0 and self.mouse.grid_position[1] <= self.height - 1:
            if self.mouse.grid_position[0] >= 0 and self.mouse.grid_position[0] <= self.width - 1:
                pg.draw.rect(self.screen, [max(channel - 55, 0) for channel in self.COLORS[self.selected]], [
                    self.mouse.grid_position.x*self.render_size + self.offset.x,
                    self.mouse.grid_position.y*self.render_size + self.offset.y,
                    self.render_size,
                    self.render_size
                ])
    
    def run(self) -> None:
        while True:
            self.handle_events()
            self.update()
            self.render()
            
            pg.display.update()
            pg.display.set_caption(f"{self.width, self.height}")
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = App()
    app.run()