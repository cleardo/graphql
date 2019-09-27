# coding=utf-8

"""
一、body或url参数形式（如：ResourceQueryVo）
1.在__init__()中初始化参数
- 对于传入的参数：使用copy_dict()方法，可以根据有传入的参数列表自动初始化该数据
- 需要初始化哪个参数就传哪个，显示指定参数名
- 使用示例：
    query_data = ResourceQueryVo(sort_type=1, name='aaa')
2.使用get()方法获取设置后的dict类型数据
注：字段名需要与接口中的参数名一模一样，这样便于使用

二、接口返回的数据（如：ChannelVo）
用于判断数据结构、与期望值做比对
"""


from data_struct.util import *

GET_CHANNEL_LIST_FAILED = '获取频道列表失败'
GET_CHANNEL_RESOURCE_BY_PAGE_FAILED = '分页查询频道资源失败'
GET_RESOURCE_GROUP_FAILED = '获取资源分组失败'
GET_ALL_CHANNELS_TAGS_TREE_FAILED = '获取所有频道的标签树失败'
DELETE_CHANNEL_TAG_FAILED = '删除频道标签失败'
UPDATE_CHANNEL_FAILED = '更新频道失败'
GET_CHANNELS_SECTIONS_FAILED = '查询频道下所有的板块信息失败'
GET_CHANNELS_TAGS_TREE_FAILED = '查询频道下的标签树失败'
GET_RESOURCE_POOL_RESOURCES_FAILED = '分页查询资源池下的资源列表失败'
GET_RESOURCE_POOL_TAGS_TREE_FAILED = '查询资源池的标签树失败'
GET_SECTION_DATA_FAILED = '获取板块下的所有数据失败'
GET_WINDOWS_SECTION_RESOURCE_LIST_FAILED = '查询橱窗推荐的资源列表失败'
SEARCH_CHANNEL_RESOURCE_BY_NAME_FAILED = '根据资源名称查询各个频道下的资源失败'


# -------------- 请求参数 --------------- #
class SearchUrlData(BaseData):
    """
    查询的url参数
    """
    def __init__(self, filter=None, order=None, offset=None, limit=None, result=None, select=None):
        """
        $filter	query	yes	过滤参数		string
        $order	query	yes	排序参数		string
        $offset	query	yes	偏移量		    string
        $limit	query	yes	记录数		    string
        $result	query	yes	返回结果格式	string
        $select	query	yes	返回结果字段	string
        """
        BaseData.__init__(self)
        self.params = copy_dict(locals())


class ResourceQueryVo(BaseData):
    """
    查询的url参数
    """

    def __init__(
            self, sort_type=None, name=None, time_status=None, status=None, is_top=None, tag_ids=None,
            group_names=None, no_tag_resource=None, page_size=None, page_no=None
    ):
        """
        sort_type	    integer (int32)	required	排序类型 1：综合 2：最新 3：最热 -> 1最新 2最热 3推荐/综合
        name	        string	        optional	资源名称，模糊查询
        time_status	    integer (int32)	optional	1即将开始 2正在开课 3已结束
        status	        integer (int32)	optional	资源状态 0下线 1上线
        is_top	        boolean	        optional	是否置顶
        tag_ids	        array[string]	optional	标签列表
        group_names	    array[string]	optional	学习单元分组列表
        no_tag_resource	boolean	        optional	是否查询未贴标签的资源, 默认为false
        page_size	    integer (int32)	optional	第几页,从0开始
        page_no	        integer (int32)	optional	每页的记录数
        """
        BaseData.__init__(self)
        self.params = copy_dict(locals())


class ChannelVoForUpdate(BaseData):
    """
    更新频道的 body参数
    - 只更新非null字段
    """

    def __init__(self, title=None, status=None, web_enabled=None, mobile_enabled=None, source_type=None,
                 web_url=None, mobile_url=None, url_redirect_mode=None):
        """
        title	            string	        optional	名称
        status	            integer (int32)	optional	状态 0下线 1上线
        web_enabled 	    boolean	        optional	web端是否启用
        mobile_enabled	    boolean	        optional	移动端是否启用
        source_type	        integer (int32)	optional	1：elearning内部 2：第三方URL
        web_url	            string	        optional	web端url地址(source_type为2时有效)
        mobile_url	        string	        optional	移动端url地址(source_type为2时有效)
        url_redirect_mode	integer (int32)	optional	url跳转方式(source_type为2时有效 1：频道内跳转 2：新窗口打开)
        """
        BaseData.__init__(self)
        self.params = copy_dict(locals())


class ResourceFindVo(BaseData):
    """
    查询频道资源 body参数
    """

    def __init__(self, name=None, channel_id=None, page_size=None, page_no=None):
        """
        name	    string	        optional	资源名称，模糊查询
        channel_id	string (uuid)	optional	频道标识
        page_size	integer (int32)	optional	第几页,从0开始
        page_no	    integer (int32)	optional	每页的记录数
        """
        BaseData.__init__(self)
        self.params = copy_dict(locals())


# ---------------- 返回值 ---------------- #
class ChannelVo(object):
    """
    频道
    """

    def __init__(self, data):
        """
        id	            string (uuid)	    optional	id
        title	        string	            optional	名称
        status	        integer (int32)	    optional	状态 0下线 1上线
        web_enabled	    boolean	            optional	web端是否启用
        mobile_enabled	boolean	            optional	移动端是否启用
        source_type	    integer (int32)	    optional	1：elearning内部 2：第三方URL
        web_url	        string	            optional	web端url地址(source_type为2时有效)
        mobile_url	    string	            optional	移动端url地址(source_type为2时有效)
        url_redirect_mode	integer (int32)	optional	url跳转方式(source_type为2时有效 1：频道内跳转 2：新窗口打开)
        create_time	    string (date-time)	optional	创建时间
        create_user	    integer (int64) 	optional	创建人
        update_time	    string (date-time)	optional	修改时间
        update_user	    integer (int64)	    optional	修改人
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('id'))
        assert_that(data, has_key('title'))
        assert_that(data, has_key('project_id'))
        assert_that(data, has_key('status'))
        assert_that(data, has_key('web_enabled'))
        assert_that(data, has_key('mobile_enabled'))
        assert_that(data, has_key('source_type'))
        assert_that(data, has_key('web_url'))
        assert_that(data, has_key('mobile_url'))
        assert_that(data, has_key('url_redirect_mode'))
        assert_that(data, has_key('create_time'))
        assert_that(data, has_key('create_user'))
        assert_that(data, has_key('update_time'))
        assert_that(data, has_key('update_user'))


class ResourceGroup(object):
    """
    学习单元分组 - 组件
    """

    def __init__(self, data):
        """
        name	string	optional	学习单元分组名称
        title	string	optional	学习单元分组标题
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('name'))
        assert_that(data, has_key('title'))


class ChannelTagTreeVo(object):
    """
    资源标签树
    """

    def __init__(self, data):
        """
        channel_id	    string (uuid)	required	频道标识
        channel_name	string	        required	频道名称
        status          int                         频道状态
        tag_tree_vo	    TagTreeVo	    optional	标签树
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('channel_id'))
        assert_that(data, has_key('channel_name'))
        assert_that(data, has_key('status'))
        assert_that(data, has_key('tag_tree_vo'))
        tag_tree_vo = data['tag_tree_vo']
        for tag_tree in tag_tree_vo:
            TagTreeVo(tag_tree)


class TagTreeVo(object):
    """
    标签树
    """

    def __init__(self, data):
        """
        id	        string (uuid)	    optional	标签标识
        title	    string	            required	标签名称
        parent_id	string (uuid)	    optional	父标签标识
        sort_number	integer (int32)	    optional	排序号
        children	array[TagTreeVo]	optional	子节点
        custom_type	string	            optional	自定义类型
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('id'))
        assert_that(data, has_key('title'))
        assert_that(data, has_key('parent_id'))
        assert_that(data, has_key('sort_number'))
        assert_that(data, has_key('children'))
        children = data['children']
        for child in children:
            TagTreeVo(child)
        assert_that(data, has_key('custom_type'))


class LearningUnitVo(object):
    """
    学习单元
    """

    def __init__(self, data):
        """
        unit_id	        string (uuid)	    optional	学习单元标识
        type	        string	            optional	学习单元类型
        external_id	    string	            optional	外部标识, e.g mooc:123
        title	        string	            optional	标题
        cover	        string	            optional	封面
        cover_url	    string	            optional	封面URL
        description 	string	            optional	描述
        start_time	    string (date-time)	optional	开始时间
        end_time	    string (date-time)	optional	结束时间
        extra	        object	            optional	额外信息
        """
        # 1.复制数据
        self.params = data
        # assert_that(data, has_key('unit_id'))
        assert_that(data, has_key('type'))
        assert_that(data, has_key('external_id'))
        assert_that(data, has_key('title'))
        assert_that(data, has_key('cover'))
        assert_that(data, has_key('cover_url'))
        assert_that(data, has_key('description'))
        assert_that(data, has_key('start_time'))
        assert_that(data, has_key('end_time'))
        assert_that(data, has_key('extra'))


class LearningUnitExtendVo(object):
    """
    学习单元 扩展信息
    """

    def __init__(self, data):
        """
        LearningUnitVo 类型的字段
        project_id	    integer (int64)	    optional	项目标识
        enabled	        boolean	            optional	上线状态
        user_count	    integer (int32)	    optional	学员人数
        create_time	    string (date-time)	optional	创建时间
        create_user	    integer (int64)	    optional	创建人
        enabled_time	string (date-time)	optional	上线时间
        is_top	        boolean	            optional	是否置顶
        top_time	    string (date-time)	optional	置顶时间
        """
        # 1.复制数据
        self.params = data
        LearningUnitVo(data)
        # assert_that(data, has_key('project_id'))
        assert_that(data, has_key('enabled'))
        assert_that(data, has_key('user_count'))
        assert_that(data, has_key('create_time'))
        assert_that(data, has_key('create_user'))
        # assert_that(data, has_key('enabled_time'))
        assert_that(data, has_key('is_top'))
        # assert_that(data, has_key('top_time'))


class ChannelResourceVo(object):
    """
    频道资源
    """

    def __init__(self, data):
        """
        resource_id	    string (uuid)	    optional	资源标识（学习单元标识）
        is_top	        boolean	            optional	是否置顶
        status	        integer (int32)	    optional	频道下状态 0下线 1上线
        create_time	    string (date-time)	optional	创建时间
        create_user	    integer (int64)	    optional	创建人
        unit_info	    LearningUnitVo	    optional	学习单元信息，需要增加热度和状态字段
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('resource_id'))
        assert_that(data, has_key('is_top'))
        assert_that(data, has_key('status'))
        assert_that(data, has_key('create_time'))
        assert_that(data, has_key('create_user'))
        assert_that(data, has_key('unit_info'))
        unit_info = data['unit_info']
        for unit in unit_info:
            LearningUnitVo(unit)


class ChannelResourceFindResultVo(object):
    """
    频道资源
    """

    def __init__(self, data):
        """
        channel_id	    string (uuid)	                optional	频道标识
        channel_name	string	                        optional	频道名称
        page	                                    	optional	资源分页信息
        - total	integer (int32)
        - items	array[LearningUnitExtendVo]
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('channel_id'))
        assert_that(data, has_key('channel_name'))
        assert_that(data, has_key('page'))
        page = data['page']
        PagerResult(page)
        items = page['items']
        for unit in items:
            LearningUnitExtendVo(unit)


class ChannelResourceFindResultVoV2(object):
    """
    频道资源
    """

    def __init__(self, data):
        """
        channel_id	    string (uuid)	                optional	频道标识
        channel_name	string	                        optional	频道名称
        page	                                    	optional	资源分页信息
        - total	integer (int32)
        - items	array[SolrResourceVoV2]
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('channel_id'))
        assert_that(data, has_key('channel_name'))
        assert_that(data, has_key('page'))
        page = data['page']
        PagerResult(page)
        items = page['items']
        for unit in items:
            SolrResourceVoV2(unit)


class SolrResourceVo(object):
    """
    搜索获得的资源详情
    """

    def __init__(self, data):
        """
        resource_id	    string (uuid)	    optional	资源标识（学习单元标识）
        title	        string	            optional	标题
        type	        string	            optional	学习单元类型
        group_names	    array[string]	    optional	学习单元分组列表
        is_top	        boolean	            optional	是否置顶
        enabled	        integer (int32)	    optional	0不可用 1可用
        user_count	    integer (int32)	    optional	热度
        external_id	    string	            optional	外部标识, e.g mooc:123
        cover	        string	            optional	封面
        cover_url	    string	            optional	封面地址
        description	    string	            optional	描述
        create_time	    string (date-time)	optional	创建时间
        create_user	    integer (int64) 	optional	创建人
        start_time	    string (date-time)	optional	开始时间
        end_time	    string (date-time)	optional	结束时间
        time_status	    integer (int32)	    optional	时间状态 1即将开始 2正在开课 3已结束
        extra	        object	            optional	额外信息
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('resource_id'))
        assert_that(data, has_key('title'))
        assert_that(data, has_key('type'))
        assert_that(data, has_key('group_names'))
        assert_that(data, has_key('is_top'))
        assert_that(data, has_key('enabled'))
        assert_that(data, has_key('user_count'))
        assert_that(data, has_key('external_id'))
        assert_that(data, has_key('cover'))
        assert_that(data, has_key('cover_url'))
        assert_that(data, has_key('description'))
        assert_that(data, has_key('create_time'))
        assert_that(data, has_key('create_user'))
        assert_that(data, has_key('start_time'))
        assert_that(data, has_key('end_time'))
        assert_that(data, has_key('time_status'))
        assert_that(data, has_key('extra'))


class SolrResourceVoV2(object):
    """
    搜索获得的资源详情
    """

    def __init__(self, data):
        """
        project_id	    integer (int64)	    optional	项目标识
        unit_id	        string (uuid)	    optional	学习单元标识
        title	        string	            optional	标题
        type	        string	            optional	学习单元类型
        is_top	        boolean	            optional	是否置顶
        enabled	        boolean	            optional	是否可用：false 不可用，true 可用
        user_count	    integer (int32)	    optional	热度
        external_id	    string	            optional	外部标识, e.g mooc:123
        cover	        string	            optional	封面
        cover_url	    string	            optional	封面地址
        description	    string	            optional	描述
        create_time	    string (date-time)	optional	创建时间
        create_user	    integer (int64) 	optional	创建人
        start_time	    string (date-time)	optional	开始时间
        end_time	    string (date-time)	optional	结束时间
        time_status	    integer (int32)	    optional	时间状态 1即将开始 2正在开课 3已结束
        extra	        object	            optional	额外信息
        visible_config	integer (int32)	    optional	可见配置 0:全部可见 1:组织内部可见
        tags	        array[TagVo]	    optional	标签信息
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('project_id'))
        assert_that(data, has_key('unit_id'))
        assert_that(data, has_key('title'))
        assert_that(data, has_key('type'))
        assert_that(data, has_key('is_top'))
        assert_that(data, has_key('enabled'))
        assert_that(data, has_key('user_count'))
        assert_that(data, has_key('external_id'))
        assert_that(data, has_key('cover'))
        assert_that(data, has_key('cover_url'))
        assert_that(data, has_key('description'))
        assert_that(data, has_key('create_time'))
        assert_that(data, has_key('create_user'))
        assert_that(data, has_key('start_time'))
        assert_that(data, has_key('end_time'))
        assert_that(data, has_key('time_status'))
        assert_that(data, has_key('extra'))
        assert_that(data, has_key('visible_config'))
        assert_that(data, has_key('tags'))


class SectionDetailVo(object):
    """
    频道板块
    """

    def __init__(self, data):
        """
        id	                string (uuid)	        optional	id
        channel_id	        string (uuid)	        optional	频道标识
        type	            integer (int32)	        optional	板块类型 1：轮播图 2：橱窗推荐 3：图标导航 4：频道内容 5：全部资源
        setting	            string	                optional	板块设置
        create_time	        string (date-time)	    optional	创建时间
        create_user	        integer (int64)	        optional	创建人
        update_time	        string (date-time)	    optional	修改时间
        update_user	        integer (int64)	        optional	修改人
        section_data_list	array[SectionDataVo]	optional	频道数据列表，轮播图、图标导航时有效
        window_data_list	array[SectionWindowDataVo]	optional	橱窗资源列表,橱窗推荐有效
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('id'))
        assert_that(data, has_key('channel_id'))
        assert_that(data, has_key('type'))
        assert_that(data, has_key('setting'))
        assert_that(data, has_key('create_time'))
        assert_that(data, has_key('create_user'))
        assert_that(data, has_key('update_time'))
        assert_that(data, has_key('update_user'))

        if data['type'] == 2:
            assert_that(data, has_key('window_data_list'))
            for window_data in data['window_data_list']:
                SectionWindowDataVo(window_data)
        elif data['type'] == 3:
            assert_that(data, has_key('section_data_list'))
            for section_data in data['section_data_list']:
                SectionDataVo(section_data)


class SectionDataVo(object):
    """
    频道板块数据
    """

    def __init__(self, data):
        """
        id	                string (uuid)	    optional	id
        section_id	        string (uuid)	    optional	板块标识
        title	            string	            optional	标题
        status	            integer (int32)	    optional	状态
        web_picture 	    string	            optional	web端图片
        web_picture_url	    string	            optional	web端图片url
        mobile_picture	    string	            optional	移动端图片
        mobile_picture_url	string	            optional	移动端图片url
        data_type	        integer (int32)	    optional	数据类型 1：标签 2：资源 3：url地址
        resource_id	        string (uuid)	    optional	资源标识（学习单元标识）
        resource_name	    string (uuid)	    optional	资源名称
        tag_id	            string (uuid)	    optional	标签标识
        tag_name	        string (uuid)	    optional	标签名称
        channel_id	        string (uuid)	    optional	资源、标签所在的频道（data_type为1、2时有效），如果是从资源池选取的，该字段为空
        channel_name	    string (uuid)	    optional	频道名称
        web_url	            string	            optional	web端url地址(dataType为3时有效)
        mobile_url	        string	            optional	移动端url地址(dataType为3时有效)
        create_time	        string (date-time)	optional	创建时间
        create_user	        integer (int64)	    optional	创建人
        update_time	        string (date-time)	optional	修改时间
        update_user	        integer (int64)	    optional	修改人
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('id'))
        assert_that(data, has_key('section_id'))
        assert_that(data, has_key('title'))
        assert_that(data, has_key('status'))
        assert_that(data, has_key('web_picture'))
        assert_that(data, has_key('web_picture_url'))
        assert_that(data, has_key('mobile_picture'))
        assert_that(data, has_key('mobile_picture_url'))
        assert_that(data, has_key('data_type'))
        assert_that(data, has_key('resource_id'))
        # assert_that(data, has_key('resource_name'))
        assert_that(data, has_key('tag_id'))
        # assert_that(data, has_key('tag_name'))
        assert_that(data, has_key('channel_id'))
        # assert_that(data, has_key('channel_name'))
        assert_that(data, has_key('web_url'))
        assert_that(data, has_key('mobile_url'))
        assert_that(data, has_key('create_time'))
        assert_that(data, has_key('create_user'))
        assert_that(data, has_key('update_time'))
        assert_that(data, has_key('update_user'))


class SectionWindowDataVo(object):
    """
    橱窗板块资源数据
    """

    def __init__(self, data):
        """
        resource_id	string (uuid)	optional	资源标识（学习单元标识）
        resource_name	string (uuid)	optional	资源名称
        picture_url	string (uuid)	optional	资源图片
        """
        # 1.复制数据
        self.params = data
        assert_that(data, has_key('resource_id'))
        assert_that(data, has_key('resource_name'))
        assert_that(data, has_key('picture_url'))
