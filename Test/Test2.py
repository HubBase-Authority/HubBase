def randfloat(self, a, b):
        """Return random integer in range [a, b], including both end points.
        """
        a = _index(float(a))
        b = _index(float(b))
        if b < a:
            raise ValueError(f"empty range in randint({a}, {b})")
        return a + self._randbelow(b - a + 1)

