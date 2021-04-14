import sys

# Given an array of disks, splice data across them, allowing for a given number of redundant disks
# This is, broadly speaking, how RAID5 and Windows Storage Spaces (SS) work

# Specify disk sizes in TB
disks = [5 / 1000000] * 4

# Number of disks which can fail without compromising the array
# To simulate SS Parity mode or RAID5, this must be 1
# For RAID6, set to 2
redundancy = 1

# How many disks to stripe each block of data across
# Parity space is calculated as (redundancy / columns), i.e. 1/3 for a typical SS parity setup
#
# You need at least as many disks as columns, and it may not be possible to fill larger disks, e.g. try disks = [2, 2, 4]
#
# SS Parity uses 3 columns by default but can be overridden if the storage pool is created in PowerShell
#
# In RAID5, columns is equal to number of disks, which is why you generally need disks of equal size
columns = 3

slab_size = 256

if len(disks) < columns:
  print("You need at least %d disks for %d columns" % (columns, columns))
  sys.exit()

if redundancy >= columns:
  print("You can only have %d redundant disks with %d columns" % (columns - 1, columns))
  sys.exit()

# All sizes from here are in MB

total = [d * 1000000 for d in disks]

print(" "*17 + "Disk %i    "*len(disks) % tuple(range(1, len(disks)+1)))

print("Total size (MB): " + "%-10s"*len(disks) % tuple(total))

taken = [0]*len(disks)

used_total = 0
space_allocated = 0

full = False

while not full:
  used_pct = [float(a) / float(b) for a, b in zip(taken, total)]

  # Find which disks to spread this slab across
  idxs = []
  for i in range(0, columns):
    idx = used_pct.index(min(used_pct))
    idxs.append(idx)
    if taken[idx] + slab_size > total[idx]:
      full = True
      break
    used_pct[idx] = 1000

  # Allocate the slab
  if not full:
    for idx in idxs:
      taken[idx] += slab_size

    used_total += (slab_size * (columns - redundancy))
    space_allocated += (slab_size * columns)

print("Space used (MB): " + "%-10s"*len(disks) % tuple(taken))
print("Utilisation (%): " + "%-10s"*len(disks) % tuple(["%0.2f%%" % ((float(a) / float(b)) * 100) for a, b, in zip(taken, total)]))

print()

print("Total space used for data:            %0.2f%% (%dGB of %dGB)" % (((float(used_total) / float(sum(total))) * 100), used_total / 1000, sum(total) / 1000))
print("Total space used for data and parity: %0.2f%% (%dGB of %dGB)" % (((float(space_allocated) / float(sum(total))) * 100), space_allocated / 1000, sum(total) / 1000))