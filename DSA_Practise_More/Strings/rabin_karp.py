# Rabin Karp Algorithm

class RabinKarpHash:
    def __init__(self, s):
        """
        This class builds PREFIX HASHES for a string `s`
        so that hash of ANY substring can be computed in O(1) time.

        --------------------------------------------------
        CORE IDEA (VERY IMPORTANT):
        --------------------------------------------------
        Hashing works like a number system.

        Decimal example:
            123 → 123 * 10 + 4 = 1234

        String hashing example:
            "ab" → hash("a") * base + value("b")

        NOTE:
        -----
        While APPENDING characters, we do NOT manually use powers.
        Multiplying by base already shifts all existing characters.
        """

        # Two large prime mod values (reduce collision chance)
        self.mod1 = 10**9 + 7
        self.mod2 = 10**9 + 9

        # Two different bases (like base-10 in numbers)
        self.base1 = 31
        self.base2 = 37

        n = len(s)

        # hash1[i] = hash of prefix s[0..i] using (base1, mod1)
        # hash2[i] = hash of prefix s[0..i] using (base2, mod2)
        self.hash1 = [0] * n
        self.hash2 = [0] * n

        # power arrays store base^i
        # These are NOT used while appending
        # They are ONLY used when REMOVING a prefix
        self.power1 = [0] * n
        self.power2 = [0] * n

        # ---------------- BASE CASE ----------------
        # First character alone forms the first prefix
        # Example: s = "abcd"
        # hash("a") = 1
        self.hash1[0] = self.charToInt(s[0])
        self.hash2[0] = self.charToInt(s[0])

        # base^0 = 1
        self.power1[0] = 1
        self.power2[0] = 1

        # ---------------- BUILD PREFIX HASHES ----------------
        for i in range(1, n):
            """
            Rolling Hash Formula:
            ---------------------
            hash(s[0..i]) = hash(s[0..i-1]) * base + value(s[i])

            WHY NO EXPLICIT POWERS HERE?
            -----------------------------
            Because multiplying by base automatically shifts powers.

            Decimal analogy:
                123 = 1*10^2 + 2*10^1 + 3*10^0
                123 * 10 = 1*10^3 + 2*10^2 + 3*10^1
                123 * 10 + 4 = 1234
            """

            # -------- FIRST HASH --------
            shifted_hash1 = self.mul(self.hash1[i - 1], self.base1, self.mod1)

            self.hash1[i] = self.add(
                shifted_hash1,
                self.charToInt(s[i]),
                self.mod1
            )

            # Precompute base^i (needed later for substring removal)
            self.power1[i] = self.mul(self.power1[i - 1], self.base1, self.mod1)

            # -------- SECOND HASH --------
            shifted_hash2 = self.mul(self.hash2[i - 1], self.base2, self.mod2)

            self.hash2[i] = self.add(
                shifted_hash2,
                self.charToInt(s[i]),
                self.mod2
            )

            self.power2[i] = self.mul(self.power2[i - 1], self.base2, self.mod2)

            """
            ---------------- EXAMPLE ITERATION ----------------
            Let s = "abcd", base = 31

            Character mapping:
                a → 1, b → 2, c → 3, d → 4

            i = 0:
                hash = 1                     ("a")
                power = 1

            i = 1 ("b"):
                hash = 1*31 + 2 = 33         ("ab")
                power = 31

            i = 2 ("c"):
                hash = 33*31 + 3 = 1026      ("abc")
                power = 961

            i = 3 ("d"):
                hash = 1026*31 + 4 = 31810   ("abcd")
                power = 29791
            """

    # --------------------------------------------------
    # Converts character to number:
    # a → 1, b → 2, ..., z → 26
    #
    # WHY +1?
    # -------
    # ord('a') - ord('a') = 0
    # Zero is BAD for hashing.
    # Adding +1 avoids zero values.
    def charToInt(self, c):
        return ord(c) - ord('a') + 1

    # Modular addition
    def add(self, a, b, mod):
        a += b
        if a >= mod:
            a -= mod
        return a

    # Modular subtraction
    def sub(self, a, b, mod):
        a -= b
        if a < 0:
            a += mod
        return a

    # Modular multiplication
    def mul(self, a, b, mod):
        return (a * b) % mod

    # --------------------------------------------------
    def getSubHash(self, l, r):
        """
        Returns hash of substring s[l..r] in O(1) time.

        Example:
            s = "abcd"
            getSubHash(1, 3) → "bcd"

        STEP-BY-STEP DERIVATION:

        Suppose:
            s = "abcd", base = 10 (for easier numbers)
            a=1, b=2, c=3, d=4
            We want hash("bcd") = s[1..3]

        Prefix hashes:
            hash("a")   = 1*10^0 = 1
            hash("ab")  = 1*10^1 + 2*10^0 = 12
            hash("abc") = 1*10^2 + 2*10^1 + 3*10^0 = 123
            hash("abcd")= 1*10^3 + 2*10^2 + 3*10^1 + 4*10^0 = 1234

        Formula:
            hash("bcd") = hash("abcd") - hash("a") * 10^3
                        = 1234 - 1*1000
                        = 234
        ✅ Correct! Powers of prefix are aligned before subtracting.

        KEY TAKEAWAY:
            * Appending characters → multiply old hash by base (powers shift automatically)
            * Removing prefix → multiply prefix hash by base^(length of substring) to align
        """

        # Step 1: take hash of prefix s[0..r]
        h1 = self.hash1[r]
        h2 = self.hash2[r]

        # If substring starts at index 0, nothing to remove
        if l == 0:
            return [h1, h2]

        # Step 2: length of substring
        length = r - l + 1

        # Step 3: remove prefix contribution (align powers)
        h1 = self.sub(
            h1,
            self.mul(self.hash1[l - 1], self.power1[length], self.mod1),
            self.mod1
        )

        h2 = self.sub(
            h2,
            self.mul(self.hash2[l - 1], self.power2[length], self.mod2),
            self.mod2
        )

        # Return double hash (collision-safe)
        return [h1, h2]


if __name__ == "__main__":
    """
    DRIVER CODE: Rabin-Karp Pattern Matching
    -------------------------------------------------
    Given a text and a pattern, find all indices where
    the pattern occurs in the text.
    """

    # Example input
    text = "ababcabcab"
    pattern = "abc"

    n = len(text)     # Length of the text = 10
    m = len(pattern)  # Length of the pattern = 3

    # Step 1: Precompute prefix hashes for the text
    # This builds the hash arrays and powers for all prefixes of text
    text_hash = RabinKarpHash(text)

    # Step 2: Compute hash for the pattern itself
    pattern_hash = RabinKarpHash(pattern)
    # pattern_hash.getSubHash(0, m-1) returns the hash of the full pattern
    p_hash = pattern_hash.getSubHash(0, m-1)

    # Step 3: Slide the pattern over the text and compare hashes
    found_indices = []  # List to store all starting indices where pattern matches

    # Loop from index 0 to n-m (last valid starting index)
    for i in range(n - m + 1):
        # Compute hash of current substring text[i..i+m-1]
        sub_hash = text_hash.getSubHash(i, i + m - 1)

        # Compare substring hash with pattern hash
        # Using double hash to reduce collision probability
        if sub_hash == p_hash:
            found_indices.append(i)

        """
        ---------------- EXAMPLE ITERATION ----------------
        text = "ababcabcab", pattern = "abc", m = 3
        We slide the pattern over text:

        i = 0: substring = "aba"
            sub_hash != pattern hash → no match

        i = 1: substring = "bab"
            sub_hash != pattern hash → no match

        i = 2: substring = "abc"
            sub_hash == pattern hash → match found at index 2
            found_indices = [2]

        i = 3: substring = "bca"
            sub_hash != pattern hash → no match

        i = 4: substring = "cab"
            sub_hash != pattern hash → no match

        i = 5: substring = "abc"
            sub_hash == pattern hash → match found at index 5
            found_indices = [2, 5]

        i = 6: substring = "bca"
            sub_hash != pattern hash → no match

        i = 7: substring = "cab"
            sub_hash != pattern hash → no match
        """

    # Step 4: Print results
    if found_indices:
        print(f"Pattern '{pattern}' found at indices: {found_indices}")
    else:
        print(f"Pattern '{pattern}' not found in the text.")

    # Expected Output for this example:
    # Pattern 'abc' found at indices: [2, 5]



