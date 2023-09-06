"""Sample pipe to view DAG and artifacts."""
import pandas as pd
from metaflow import FlowSpec, step


class SampleFlow(FlowSpec):
    """Sample Metaflow Flow"""

    @step
    def start(self):
        """Start step"""
        self.x = 1
        print("MF pipe is starting.")
        self.next(self.p1, self.p2)

    @step
    def p1(self):
        """First parallel step"""
        self.hi = pd.DataFrame([{"hello": "there"}])
        print("Executing first parallel step.")
        self.next(self.join)

    @step
    def p2(self):
        """Second parallel step"""
        print("Executing second parallel step.")
        self.next(self.join)

    @step
    def join(self, artifacts):
        """Join step"""
        print("Executing join step.")
        self.next(self.end)

    @step
    def end(self):
        """End step"""
        print("MF pipe is all done.")


if __name__ == "__main__":
    SampleFlow()
