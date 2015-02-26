from django.test import TestCase, RequestFactory
from jb_blog.views import post_detail
from jb_blog.models import Post


# Create your tests here.
class post_list(TestCase):
	fixtures = ['post_testdata.json']
	def test_post_list(self):

		self.client.login(username='j', password='j')
		resp = self.client.get('/blog/')
		self.assertTrue('all_posts', 'user' in resp.context)
		p_1 = resp.context['all_posts'][0]
		#print resp.content


	def test_post_detail(self):
		
		slug = 'another-test-post'
		post = Post.objects.get(slug=slug)
		self.client.login(username='j', password='j')
		r = self.client.get(post.get_absolute_url(), {'object': 'object'})
		print r.context['post'].published

		# response = post_detail.as_view()(request, slug='another-test-post')
		# print response

