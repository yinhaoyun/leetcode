package com.haoyun.leetcode;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MaximumSwapTest {
    @Test
    void test() {
        MaximumSwap ms = new MaximumSwap();

        // https://leetcode.com/problems/maximum-swap/description/
        assertEquals(7236, ms.maximumSwap(2736));
        assertEquals(9973, ms.maximumSwap(9973));

        // My Test Case
        assertEquals(4321, ms.maximumSwap(4321));
        assertEquals(4321, ms.maximumSwap(3421));
        assertEquals(4321, ms.maximumSwap(2341));
        assertEquals(4321, ms.maximumSwap(1324));
        assertEquals(4321, ms.maximumSwap(4123));

    }

}