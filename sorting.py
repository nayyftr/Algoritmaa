def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

merge_sorted_array = X.copy()
merge_sort(merge_sorted_array)
print("Merge Sorted Array:", merge_sorted_array)

quick_sorted_array = quick_sort(X.copy())
print("Quick Sorted Array:", quick_sorted_array)

def complexity_analysis():
    print("\nComplexity Analysis:")
    print("Merge Sort:")
    print("- Average Case: O(n log n)")
    print("\nQuick Sort:")
    print("- Average Case: O(n log n)")

complexity_analysis()


# Merge Sort:
# 1. Best Case selalu membagi array menjadi dua bagian yang sama, tanpa bergantung pada urutan elemen di dalam array, Proses penggabungan (merge) tetap memerlukan waktu O(n) karena setiap elemen harus dibandingkan dan digabungkan kembali.
# 2. Worst Case pembagian dan penggabungan tetap terjadi secara konsisten. Tidak ada skenario di mana Merge Sort memerlukan lebih banyak langkah untuk elemen-elemen tertentu.
# 3. Averange Case rata-rata kasus mencerminkan sifat stabil dari Merge Sort, yang tidak terpengaruh oleh urutan awal elemen.

# Quick Sort:
# 1. Best Case terjadi ketika pivot yang dipilih selalu membagi array menjadi dua bagian yang hampir sama besar, dengan pembagian yang optimal seperti ini, hanya diperlukan O(logn) tingkat rekursi, dan setiap tingkat memproses O(n) elemen.
# 2. Worst Case Terjadi ketika pivot yang dipilih adalah elemen terkecil atau terbesar secara konsisten, akibatnya satu bagian akan kosong, sementara bagian lain berisi n−1 elemen, menyebabkan pembagian yang sangat tidak efisien.
# 3. Averange Case secara rata-rata, pivot yang dipilih akan membagi array menjadi dua bagian yang tidak terlalu berbeda ukurannya.
