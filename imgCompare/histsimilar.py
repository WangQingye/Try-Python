#!/usr/bin/python
# -*- coding: utf-8 -*-

import Image

def make_regalur_image(img, size = (256, 256)):
	return img.resize(size).convert('RGB')

def split_image(img, part_size = (64, 64)):
	w, h = img.size
	pw, ph = part_size
	
	assert w % pw == h % ph == 0
	
	return [img.crop((i, j, i+pw, j+ph)).copy() \
				for i in xrange(0, w, pw) \
				for j in xrange(0, h, ph)]

def hist_similar(lh, rh):
	assert len(lh) == len(rh)
	return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

def calc_similar(li, ri):
#	return hist_similar(li.histogram(), ri.histogram())
	return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0
			

def calc_similar_by_path(lf, rf):
	li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
	return calc_similar(li, ri)

def make_doc_data(lf, rf):
	li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
	li.save(lf + '_regalur.png')
	ri.save(rf + '_regalur.png')
	fd = open('stat.csv', 'w')
	fd.write('\n'.join(l + ',' + r for l, r in zip(map(str, li.histogram()), map(str, ri.histogram()))))
#	print >>fd, '\n'
#	fd.write(','.join(map(str, ri.histogram())))
	fd.close()
	import ImageDraw
	li = li.convert('RGB')
	draw = ImageDraw.Draw(li)
	for i in xrange(0, 256, 64):
		draw.line((0, i, 256, i), fill = '#ff0000')
		draw.line((i, 0, i, 256), fill = '#ff0000')
	li.save(lf + '_lines.png')
	

if __name__ == '__main__':
	path = r'test/TEST1/%d.JPG'
	for i in xrange(1, 7):
		calc_similar_by_path('test/TEST1/1.JPG', 'test/TEST1/1.JPG'%(i, 2)))
	
#	make_doc_data('test/TEST4/1.JPG', 'test/TEST4/2.JPG')

