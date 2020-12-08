from helper import lines_from_day
from functools import cache

def parse():
    for line in lines_from_day(8):
        instruction, operand = line.split(" ")
        yield (instruction, int(operand))

class Machine:
    def __init__(self, program):
        self.prog = program # list of (instruction, operand)
        self.accu = 0
        self.prcn = 0
        self.visited = set()

    def acc(self, n):
        self.accu += n
    def jmp(self, n):
        self.prcn += n-1
    def nop(self, _):
        pass

    def run(self, start=0):
        self.prcn = start
        while (self.prcn not in self.visited) \
          and (0<=self.prcn<len(self.prog)):
            self.visited.add(self.prcn)
            inst, op = self.prog[self.prcn]
            { "acc": self.acc,
              "jmp": self.jmp,
              "nop": self.nop, }[inst](op)
            self.prcn += 1
        return (self.prcn not in self.visited)

    def postmortem(self):
        if (self.prcn not in self.visited): # if finished.
            print(f"Reached end of program with acc={self.accu}.")
        else:
            inst, op = self.prog[self.prcn]
            print(f"Cancelled with acc={self.accu} after" \
                 +f" entering an infinite loop from {inst} {op}" \
                 +f" at {self.prcn}.")

program = list(parse())

print("Part 1:", end=' ')
m = Machine(program)
m.run()
m.postmortem()

class Repairer:
    def __init__(self, program):
        self.prog = program

    def search(self): # brute force ...
        for (i, (instr, op)) in enumerate(self.prog):
            pm = self.prog.copy()
            if instr == "acc": continue
            else:
                ni = ("jmp" if (instr == "nop") else "nop")
                pm[i] = [ni, op]
            if (m := Machine(pm)).run():
                m.postmortem()
                break

print("Part 2:")
rp = Repairer(program)
rp.search()
