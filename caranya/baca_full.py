import json

with open('quran-ayah') as f:
    quran = json.load(f)

basmalah = quran['data'][0]['kitabah']
surat_arab = quran['data'][0]['surah']['arabic']

with open('quran_kemenag.txt', 'w') as j:
	j.write('bismillah\n\n')

angka_arab='٠١٢٣٤٥٦٧٨٩'
def angka_ke_angka_arab(angka):
	return ''.join([angka_arab[int(a)] for a in str(angka)])

ayat_arab = '\n' + '='*30 + '\njuz 1\n' + '-'*30 + '\nhalaman 1\n\n' + 'سورة ' + surat_arab + '\n'
juz = 1
page = 1
surah_id = 1

for id in range(6236):
# for id in range(50):

	
	ayats = quran['data'][id]
	surah_id_prev = surah_id
	surah_id = ayats['surah_id']

	
	page_prev = page
	page = ayats['page']

	
	kitabah = ayats['kitabah']
	ayat_ke = ayats['ayah']
	ayat_ke_arab = angka_ke_angka_arab(ayat_ke)

	surats = ayats['surah']
	surat_indonesia = surats['transliteration']
	surat_arab = surats['arabic']



	if page != page_prev:
		if (page - 2) % 20 == 0 and page > 20:
			juz += 1
			ayat_arab = ayat_arab + '\n' + '='*30 + '\njuz ' + str(juz) + '\n'
			
		ayat_arab = ayat_arab + '\n' + '-'*30 + '\nhalaman ' + str(page) + '\n\n'

	if surah_id != surah_id_prev:
		ayat_arab = ayat_arab +'\n' + 'سورة ' + surat_arab + '\n' + basmalah + '\n'

	# print('halaman ', page, 'surat ke', surah_id, kitabah)
	# print()
	
	
		# ~ break
	
	ayat_arab = ayat_arab + ' ' + kitabah + ' ' + ayat_ke_arab

	if (page - 2) % 20 == 0 and page > 20:
		
		with open('quran_kemenag.txt', 'a') as j:
			j.write(ayat_arab)
		
		ayat_arab = ''
		# ~ break
		# ~ juz += 1
		# ~ ayat_arab = '\njuz ' + str(juz) + '\n'

print(ayat_arab)
with open('quran_kemenag.txt', 'a') as j:
	j.write(ayat_arab)


    
# print(ayat)
