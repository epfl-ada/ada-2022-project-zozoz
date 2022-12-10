import adapter from '@sveltejs/adapter-static';
import { mdsvex } from 'mdsvex';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: ['.svelte', '.md', '.svx'],
	preprocess: [
		mdsvex({
			extensions: ['.md', '.svx'],
		})
	],
	kit: {
		paths: { base: '/ada-2022-project-zozoz' },
		adapter: adapter()
	}
};

export default config;
