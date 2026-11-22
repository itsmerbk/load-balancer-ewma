class EWMALoadBalancer:
    def __init__(self, nodes, alpha=0.3):
        self.lat, self.alpha = {n: 10.0 for n in nodes}, alpha
    def record(self, node, ms): self.lat[node] = self.alpha*ms + (1 - self.alpha)*self.lat[node]
    def pick(self): return min(self.lat, key=self.lat.get)

if __name__ == "__main__":
    lb = EWMALoadBalancer(["srv1", "srv2"]); lb.record("srv1", 90.0); lb.record("srv2", 5.0)
    assert lb.pick() == "srv2"
    print("[PASS] 099_load_balancer_ewma")
