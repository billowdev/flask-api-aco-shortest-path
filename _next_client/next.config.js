/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ["localhost", 'localhost:5000', 'fastly.picsum.photos', 'picsum.photos', process.env.NEXT_PUBLIC_IMAGE_HOST || ''],
  },
}

module.exports = nextConfig


