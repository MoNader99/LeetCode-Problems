merge = (nums1, m, nums2, n) =>{
let i = m-1;
let j = n-1;
let mn = m+n - 1;
while(i>=0 && j>=0){
    if(nums1[i] > nums2[j]){
        nums1[mn] = nums1[i];
        i--;
    }
    else{
        nums1[mn] = nums2[j];
        j--;
    }
    mn--;
}
while(j>=0){
    nums1[mn] = nums2[j];
    j--;
    mn--; 
}
}


// Example 1:
let nums1 = [1, 2, 3, 0, 0, 0];
let m = 3;
let nums2 = [2, 5, 6];
let n = 3;
merge(nums1, m, nums2, n);
console.log(nums1);  // Output: [1, 2, 2, 3, 5, 6]

console.log("----------------------------------");

// Example 2:
nums1 = [1];
m = 1;
nums2 = [];
n = 0;
merge(nums1, m, nums2, n);
console.log(nums1);  // Output: [1]

console.log("----------------------------------");

// Example 3:
nums1 = [0];
m = 0;
nums2 = [1];
n = 1;
merge(nums1, m, nums2, n);
console.log(nums1);  // Output: [1]