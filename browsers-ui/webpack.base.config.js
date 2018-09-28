/*
	webpack将所有的文件当作js文件来处理，主要是通过一个入口文件，查找相应的依赖，遇见不是js的文件借助相应的loader来进行处理，打包输出到统一的js文件中。
	webpack基于模块化打包的工具。同时它的核心功能有许多的插件以及loader，来处理我们的文件。
*/

const CleanWebpackPlugin = require('clean-webpack-plugin');
const path = require('path');
const webpack = require('webpack');
const htmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
	entry: {
		vendor: ['react', 'react-dom'],
		index: path.resolve(__dirname, "src/index.js")
	},
	output: {
		path: path.resolve(__dirname, "dist/"),    // 打包好的文件输出的路径
		filename: "js/[name].[hash:8].js",
		// publicPath: "/dist",                  // 指定 HTML 文件中资源文件 (字体、图片、JS文件等) 的文件名的公共 URL 部分的
		chunkFilename: 'js/[name].[hash:8].js'      // 按需加载时打包的chunk
	},
	module: {
		rules: [
			{
				test: /.(js|jsx)$/,
				use: [{
					loader: 'babel-loader',
					options: {presets: ["react", ["env", {"modules": false}]]}
				}],
				exclude: path.resolve(__dirname, "node_modules")  // 排除node_modules下的文件
			},
			{
				test: /\.css$/,
				exclude: /node_modules/,
				use: [
					"style-loader",
					"css-loader",
				]
			},
			{
				test: /\.less$/,
				exclude: /node_modules/,
				use: [
					"style-loader",
					"css-loader",
					"less-loader"
				]
			},
			{
        test: /\.scss$/,
        exclude: /node_modules/,
        use: [
					"style-loader",
					"css-loader",
					"sass-loader"
				]
      },
			{
				test: /\.(gif|png|jpe?g)$/,
				use: [{
					loader: "file-loader",
					options: {
						name: "static/img/[name].[ext]"
					}
				}]
			},
			{
				test: /\.(ttf|eot|svg|woff)(\?(\w|#)*)?$/,
				use: [{
					loader: "file-loader",
					options: {
						name: "static/font/[name].[ext]"
					}
				}]
			}
		]
	},
	resolve: {
		modules:[path.resolve(__dirname,'src'),'node_modules'],   // 将src添加到搜索目录，且src目录优先'node_modules'搜索。modules: [],告诉 webpack 解析模块时应该搜索的目录.默认为node——modules
		extensions: [".js", ".jsx", ".css", ".less", '.scss'],    // 自动解析确定的扩展名（js/jsx/json),能够使用户在引入模块时不带扩展
		alias: {                                                  // 创建 import 或 require 的别名，来确保模块引入变得更简单
			"components": path.resolve(__dirname, 'src/components/'),
			"containers": path.resolve(__dirname, 'src/containers/'),
			"assets": path.resolve(__dirname, "src/assets/"),
			"actions": path.resolve(__dirname, 'src/actions/'),
			"reducers": path.resolve(__dirname, 'src/reducers/'),
			"utils": path.resolve(__dirname, 'src/utils/'),
		}
	},
	plugins: [
		require('autoprefixer'),    // 自动补全css前缀
		new htmlWebpackPlugin({     // 自动创建html
			template: 'index.html',   // 创建html所引用的模板，默认为根目录下的html
			title: "",  							// 传参，模板中可通过<%= htmlWebpackPlugin.options.title%>来获取
			filename: "index.html",   // 创建后的html的文件名
			// inject: true           // 注入打包好的js,默认为true。 可通过  inject: head/body  声明将js注入到模板中的head/body标签中
		}),
		new webpack.optimize.CommonsChunkPlugin(['vendor']),  // 将公用的模块抽取到vendor文件中
		new CleanWebpackPlugin('dist/', { verbose: false }),    // 每次打包时，将之前打包生成的文件都删除
		new webpack.optimize.UglifyJsPlugin({                 // 压缩打包的js文件
			sourceMap: true,                                    // 当你的js编译压缩后，需要继续读取原始脚本信息的行数，位置，警告等有效调试信息时,手动开启UglifyJsPlugin 的配置项：sourceMap: true
			compress: {
				warnings: false
			}
		}),
		new webpack.ProvidePlugin({ // 配置全局的jquery
			$:"jquery",
			jQuery:"jquery",
			"window.jQuery":"jquery"
		})
	],
};