function cavityMap(grid) {
    for (let i = 1; i < grid.length - 1; i++) {
        let nums = grid[i].split('')
        for (let j = 1; j < nums.length - 1; j++) {
            if (nums[j] > grid[i-1].charAt(j) && nums[j] > grid[i].charAt(j-1) && nums[j] > grid[i].charAt(j+1) && nums[j] > grid[i+1].charAt(j)) {
                nums[j] = 'X'
            }
        }
        grid[i] = nums.join('')
    }    
    return grid
}

console.log(cavityMap(['1112','1912','1892','1234']))