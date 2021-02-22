from pytube import YouTube

link = input("Enter the youtube link here:\n")

you_tube = YouTube(link)

print(f"\nTitle: {you_tube.title}")

print(f"\nRating: {you_tube.rating}")

print(f"\nViews: {you_tube.views}")

print(f"\nVideo Length: {you_tube.length} seconds")

print(f"\nDiscription: {you_tube.description}\n")

video = you_tube.streams.get_highest_resolution()

print("downloading...")

video.download()

print("Download complete!")

