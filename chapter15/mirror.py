class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write