import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data_2", delimiter=" ")
df_new = df.set_index("size")

df_new[["insertion","quicksort","heapsort","radixsort"]].plot(linewidth=4)
plt.savefig("plt1.png")
df_new[["insertion_sorted","quicksort_sorted","heapsort_sorted","radixsort_sorted"]].plot(linewidth=4)
plt.savefig("plt2.png")


small = df_new[18:]

small[["quicksort","heapsort","radixsort"]].plot(linewidth=4)
plt.savefig("plt3.png")
small[["quicksort_sorted","heapsort_sorted","radixsort_sorted"]].plot(linewidth=4)
plt.savefig("plt4.png")


